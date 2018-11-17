# Learn The Spire

Neural Network for choosing between cards in Slay the Spire.

## Requirements

`python3` and `pip3`

```bash
pip3 install -r requirements.txt
```

I don't know the path for the where the past runs are stored for systems besides MacOS, so it can only locate runs on MacOS at the moment.

## Main Idea

- Scrapes local run data into `IRONCLAD_TRAINING_DATA`, `THE_SILENT_TRAINING_DATA`, and `DEFECT_TRAINING_DATA`, using `get_training_data.py`, and encoding cards into 1 x 234 vectors with `card_name_to_vector.py`.

```bash
python3 get_training_data.py
2018-11-17 11:23:33,921 - learnthespire - INFO - Found 33 IRONCLAD runs
2018-11-17 11:23:43,529 - learnthespire - INFO - Found 1 DEFECT runs
2018-11-17 11:23:43,722 - learnthespire - INFO - Found 4 THE_SILENT runs
```

- Train a feed-forward neural network with our past run data with `train_model.py`, using the supplied training data file.

```bash
python3 train_model.py IRONCLAD_TRAINING_DATA
2018-11-17 12:56:13,213 - learnthespire - INFO - Epoch 1 completed out of 10 loss: 2979.932667877604
2018-11-17 12:56:13,495 - learnthespire - INFO - Epoch 2 completed out of 10 loss: 1761.6639074202915
2018-11-17 12:56:13,777 - learnthespire - INFO - Epoch 3 completed out of 10 loss: 1344.5543219195952
2018-11-17 12:56:14,061 - learnthespire - INFO - Epoch 4 completed out of 10 loss: 1101.1279998984428
2018-11-17 12:56:14,341 - learnthespire - INFO - Epoch 5 completed out of 10 loss: 934.2588043879878
2018-11-17 12:56:14,623 - learnthespire - INFO - Epoch 6 completed out of 10 loss: 809.4915486584464
2018-11-17 12:56:14,904 - learnthespire - INFO - Epoch 7 completed out of 10 loss: 709.3352899401771
2018-11-17 12:56:15,187 - learnthespire - INFO - Epoch 8 completed out of 10 loss: 626.7456984166201
2018-11-17 12:56:15,472 - learnthespire - INFO - Epoch 9 completed out of 10 loss: 561.5867884071777
2018-11-17 12:56:15,752 - learnthespire - INFO - Epoch 10 completed out of 10 loss: 509.7387458057201
2018-11-17 12:56:15,967 - learnthespire - INFO - Accuracy: 41.605839416058394%
```

- Store and use the model to tell us which card to pick.

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.

## Credit

The structure of the neural network is heavily based on the one created in [sentdex's series on neural networks](https://www.youtube.com/watch?v=oYbVFhK_olY).
