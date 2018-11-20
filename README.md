# Learn The Spire

Neural Network for choosing between cards in Slay the Spire using Tensorflow.

## Requirements

`python3` and `pip3`

```bash
pip3 install -r requirements.txt
```
Should be able to locate runs on Windows and macOS.

## Main Idea

- Scrapes local run data into `IRONCLAD_TRAINING_DATA`, `THE_SILENT_TRAINING_DATA`, and `DEFECT_TRAINING_DATA`, using `get_training_data.py`, and encoding cards into 1 x 234 vectors with `card_name_to_vector.py`.

```bash
python3 get_training_data.py
2018-11-17 11:23:33,921 - learnthespire - INFO - Found 33 IRONCLAD runs
2018-11-17 11:23:43,529 - learnthespire - INFO - Found 1 DEFECT runs
2018-11-17 11:23:43,722 - learnthespire - INFO - Found 4 THE_SILENT runs
```

- Train a feed-forward neural network with our past run data with `train_model.py`, using the supplied training data file and save it to the disk.

```bash
python3 train_model.py IRONCLAD_TRAINING_DATA
2018-11-18 07:43:54.581548: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2018-11-18 07:43:54,830 - learnthespire - INFO - Epoch 1 completed out of 100 loss: 650.9242441654205
2018-11-18 07:43:54,873 - learnthespire - INFO - Epoch 2 completed out of 100 loss: 550.7045561671257
2018-11-18 07:43:54,920 - learnthespire - INFO - Epoch 3 completed out of 100 loss: 473.46800112724304
...
2018-11-18 07:43:59,346 - learnthespire - INFO - Epoch 98 completed out of 100 loss: 19.377360731363297
2018-11-18 07:43:59,393 - learnthespire - INFO - Epoch 99 completed out of 100 loss: 19.127103462815285
2018-11-18 07:43:59,439 - learnthespire - INFO - Epoch 100 completed out of 100 loss: 18.884481981396675
2018-11-18 07:43:59,507 - learnthespire - INFO - Accuracy: 80.0000011920929%
2018-11-18 07:43:59,590 - learnthespire - INFO - Model saved to ./models/IRONCLAD.model
```

After a hundred epochs, which takes around 5 seconds with this small dataset, we can train a neural network that chooses the same as a human player around 80% of the time.

At around 500 epochs, it can pick with what seems to be 100% accuracy on the dataset, but in reality it's probably much lower because the testing and training sets are the same and there's a small dataset so there could be overfitting.

- Load the model and use it to tell us which card to pick.

```bash
python3 load_model.py IRONCLAD.model
Card 1: barricade
Card 2: limit break
Card 3: offering
The Neural Network chooses: Limit Break
Card 1: shrug it off
Card 2: true grit
Card 3: flex
The Neural Network chooses: True Grit
```

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.

## Credit

The structure of the neural network is heavily based on the one created in [sentdex's series on neural networks](https://www.youtube.com/watch?v=oYbVFhK_olY).
