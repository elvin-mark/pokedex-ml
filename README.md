# pokedex-ml
Simple Pokedex App using Flask for the backend and ReactJS for the frontend. A simple convolutional neural network was used to train on images found in the [kaggle dataset of pokemon images ](https://www.kaggle.com/lantian773030/pokemonclassification). The network was train using the [trainer](https://github.com/elvin-mark/pytorch_trainer) from my other repo.
You can upload the image of a pokemon or take a picture of a pokemon using the camera and then get which pokemon is it along with some extra data.

# How to run
Run the following command line in your terminal (or command prompt)
```
python server.py
```
If you have ngrok, you can run the following line in order to not just use this app locally but from outside your local network.
```
ngrok http 5000
```

![pokedex](samples/pokedex.png?raw=true "Pokedex Sample")