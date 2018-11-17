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
2018-11-17 13:54:03,478 - learnthespire - INFO - Epoch 1 completed out of 100 loss: 590.5297908782959
2018-11-17 13:54:03,521 - learnthespire - INFO - Epoch 2 completed out of 100 loss: 475.7371578216553
2018-11-17 13:54:03,563 - learnthespire - INFO - Epoch 3 completed out of 100 loss: 399.78688859939575
...
2018-11-17 13:54:07,880 - learnthespire - INFO - Epoch 98 completed out of 100 loss: 13.908400133252144
2018-11-17 13:54:07,928 - learnthespire - INFO - Epoch 99 completed out of 100 loss: 13.723397821187973
2018-11-17 13:54:07,974 - learnthespire - INFO - Epoch 100 completed out of 100 loss: 13.521378010511398
2018-11-17 13:54:08,040 - learnthespire - INFO - Accuracy: 82.14285969734192%
```

After a hundred epochs, which takes around 5 seconds on my computer with this small dataset, we can train a neural network that chooses the same as a human player 82% of the time!

- Store and use the model to tell us which card to pick.

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.

## Credit

The structure of the neural network is heavily based on the one created in [sentdex's series on neural networks](https://www.youtube.com/watch?v=oYbVFhK_olY).
