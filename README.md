# Learn The Spire

Neural Network for choosing which card to pick or whether or not to pick a card at all in Slay the Spire.

## Main Idea

- Scrapes local run data into `IRONCLAD_TRAINING_DATA`, `THE_SILENT_TRAINING_DATA`, and `DEFECT_TRAINING_DATA`, using `get_training_data.py`.

- Encoding cards into 1 x 124 vectors with `card_name_to_vector.py`.

```python
from card_name_to_vector import card_name_to_vector

card_name_to_vector('Bash')
[[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''
1st position is card cost
Followed by the count of how many times each word in the Slay the Spire "vocabulary" shows up within the card
'''
```

- Feed 3 cards into the neural network and compare the neural network's result to what you picked in your run and use an optimizer function to modify the network to get closer to what you picked, partially implemented in `train_model.py`. Do this for a while until we're satisfied and then save the model for usage.

  - Finished neural network structure, now to work on training.
  
    ```bash
    # asks random untrained model to choose between Bash (1st), Strike (2nd), Defend (3rd), and skipping
    python3 train_model.py
    #   skip           1st         2nd         3rd
    [[-15.79862    -1.3561792  -1.8212131   4.652817 ]]
    ```

- Use the model to tell us which card to pick!

- Go back and evolve this to take more inputs like our existing deck, and maybe even support choosing choices at random events and route choices.

- Fully automated AI Slay the Spire player.
