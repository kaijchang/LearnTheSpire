# Learn The Spire

Neural Network for choosing which card to pick or whether or not to pick a card at all in Slay the Spire.

## Requirements

```bash
pip3 install -r requirements.txt
```

## Main Idea

- Scrapes local run data into `IRONCLAD_TRAINING_DATA`, `THE_SILENT_TRAINING_DATA`, and `DEFECT_TRAINING_DATA`, using `get_training_data.py`, and encoding cards into 1 x 234 vectors with `card_name_to_vector.py`.

```bash
python3 get_training_data.py
2018-11-17 11:23:33,921 - learnthespire - INFO - Found 33 IRONCLAD runs
2018-11-17 11:23:43,529 - learnthespire - INFO - Found 1 DEFECT runs
2018-11-17 11:23:43,722 - learnthespire - INFO - Found 4 THE_SILENT runs
```

- Train a feed-forward neural network with our past run data, using `train_model.py`, using the supplied training data file.

```bash
python3 train_model.py IRONCLAD_TRAINING_DATA
2018-11-17 11:20:10,628 - learnthespire - INFO - Epoch 1 completed out of 10 loss: 2664.625208620518
2018-11-17 11:20:10,922 - learnthespire - INFO - Epoch 2 completed out of 10 loss: 2040.6023952979883
2018-11-17 11:20:11,225 - learnthespire - INFO - Epoch 3 completed out of 10 loss: 1639.6153593958861
2018-11-17 11:20:11,522 - learnthespire - INFO - Epoch 4 completed out of 10 loss: 1347.4823346473759
2018-11-17 11:20:11,828 - learnthespire - INFO - Epoch 5 completed out of 10 loss: 1124.945190030243
2018-11-17 11:20:12,114 - learnthespire - INFO - Epoch 6 completed out of 10 loss: 960.7809153368064
2018-11-17 11:20:12,394 - learnthespire - INFO - Epoch 7 completed out of 10 loss: 836.0690773178535
2018-11-17 11:20:12,673 - learnthespire - INFO - Epoch 8 completed out of 10 loss: 739.9554662491839
2018-11-17 11:20:12,955 - learnthespire - INFO - Epoch 9 completed out of 10 loss: 661.8177415163109
2018-11-17 11:20:13,225 - learnthespire - INFO - Epoch 10 completed out of 10 loss: 595.17589914054
```

Look at the loss decreasing! This means our model is getting better at predicting what we would pick.

- Store and use the model to tell us which card to pick!

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.

## Credit

The structure of the neural network is heavily based on the one created in [sentdex's series on neural networks](https://www.youtube.com/watch?v=oYbVFhK_olY).
