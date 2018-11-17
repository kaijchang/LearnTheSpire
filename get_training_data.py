import sys
import os

import json

if sys.platform == 'darwin':
    runs_directory = os.path.expanduser(
        '~/Library/Application Support/Steam/steamapps/common/SlayTheSpire/SlayTheSpire.app/Contents/Resources/runs')

else:
    raise NotImplementedError


for character_folder in os.listdir(runs_directory):
    if not os.path.exists('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder)):
        with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder),
                  'w') as training_data_file:
            json.dump([], training_data_file)

    for run_file in os.listdir(os.path.join(runs_directory, character_folder)):
        with open(os.path.join(runs_directory, character_folder, run_file)) as run:
            with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder)) as training_data_file:
                training_data = json.load(training_data_file)

            training_data += json.load(run)['card_choices']

            with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder), 'w') as training_data_file:
                json.dump(training_data, training_data_file)
