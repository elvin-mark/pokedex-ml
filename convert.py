from multiprocessing import dummy
import torch
from models import pokemon_model

dev = torch.device("cpu")
model = pokemon_model().to(dev)
model.load_state_dict(torch.load("model/pokemon_cnn.ckpt", map_location=dev))
model.eval()

dummy = torch.zeros(1, 3, 112, 112)
torch.onnx.export(model, dummy, "model/pokemon_cnn.onnx", verbose=True)
