import torch
import torch.nn as nn
import torchvision
import PIL
import pickle
from flask import Flask, request, render_template
import pandas as pd
import json
import base64
from io import BytesIO
from models import pokemon_model

dev = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_cnn = pokemon_model().to(dev)

with open("data/pokemon_label.pkl", "rb") as f:
    labels_ = pickle.load(f)
# labels_ = {v: k for k, v in labels.items()}

model_cnn.load_state_dict(torch.load(
    "model/pokemon_cnn.ckpt", map_location=torch.device('cpu')))

# test_transform = torchvision.transforms.Compose([
#     torchvision.transforms.Resize(256),
#     torchvision.transforms.CenterCrop((224, 224)),
#     torchvision.transforms.ToTensor(),
#     torchvision.transforms.Normalize(
#         (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
# ])

test_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((112, 112)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.49139968, 0.48215827, 0.44653124], [
        0.24703233, 0.24348505, 0.26158768])
])

model_cnn.eval()

pokemon_df = pd.read_csv("data/pokemon.csv")

soft_max = nn.Softmax(dim=1)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pokemon", methods=["GET", "POST"])
def get_pokemon():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        if len(request.files) > 0:
            I = PIL.Image.open(request.files["pokemon_image"]).convert("RGB")
        elif len(request.form) > 0:
            I = PIL.Image.open(BytesIO(base64.b64decode(
                request.form["pokemon_image"][23:]))).convert("RGB")
        else:
            return "Error!"
        x = test_transform(I)
        y = model_cnn(x.reshape(-1, *x.shape))
        y_prob = soft_max(y)
        idxs = torch.argsort(y[0], descending=True)[:10]
        possible_pokemons = [labels_[idx.item()] for idx in idxs]
        response = {}
        for pokemon, prob in zip(possible_pokemons, y_prob[0][idxs]):
            results_db = pokemon_df.loc[pokemon_df["name"] == pokemon]
            if len(results_db) > 0:
                with open(f"pokemon/images/{pokemon.lower()}.png", "rb") as f:
                    img_b64 = base64.b64encode(f.read())
                response[pokemon] = {}
                response[pokemon]["confidence"] = prob.item() * 100
                response[pokemon]["data"] = results_db.iloc[0].to_json()
                response[pokemon]["image"] = str(img_b64)[2:-1]
        print(possible_pokemons)
        return json.dumps(response)

    else:
        return "Error!"


if __name__ == "__main__":
    app.run()
