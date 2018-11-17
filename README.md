# Learn The Spire

Neural Network for choosing which card to pick or whether or not to pick a card at all in Slay the Spire.

## Requirements

```bash
pip3 install -r requirements.txt
```

## Main Idea

- Scrapes local run data into `IRONCLAD_TRAINING_DATA`, `THE_SILENT_TRAINING_DATA`, and `DEFECT_TRAINING_DATA`, using `get_training_data.py`.

- Encoding cards into 1 x 124 vectors with `card_name_to_vector.py`.

```bash
python3 card_name_to_vector.py
```

- Train a feed-forward neural network with our past run data, using `train_model.py`.

```bash
python3 train_model.py
Epoch 1 completed out of 10 loss: 3810.269546604537
Epoch 2 completed out of 10 loss: 2484.9399606699276
Epoch 3 completed out of 10 loss: 1977.1163812771513
Epoch 4 completed out of 10 loss: 1597.0395948176538
Epoch 5 completed out of 10 loss: 1322.8860301747236
Epoch 6 completed out of 10 loss: 1115.8326343670508
Epoch 7 completed out of 10 loss: 952.1410382498252
Epoch 8 completed out of 10 loss: 821.1171007922635
Epoch 9 completed out of 10 loss: 717.6960411003183
Epoch 10 completed out of 10 loss: 634.1040910915835
```

Look at the loss decreasing! This means our model is getting better at predicting what we would pick.

- Store and use the model to tell us which card to pick!

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.

## Credit

The structure of the neural network is heavily based on the one created in [sentdex's series on neural networks](https://www.youtube.com/watch?v=oYbVFhK_olY).
