import sys
import os

import json
import random

from card_name_to_vector import card_name_to_vector
from learnthespirelogger import logger


def choice_dict_to_vectors(choice_dict, relics):
    if choice_dict['picked'] == 'SKIP':
        if len(choice_dict['not_picked']) != 3:
            print(choice_dict, relics)
        return [[card_name_to_vector(card_name) for card_name in choice_dict['not_picked']], [[1, 0, 0, 0]]]

    else:
        choices = choice_dict['not_picked'] + [choice_dict['picked']]
        random.shuffle(choices)
        if len(choices) != 3:
            print(choice_dict, relics)
        return [
            [card_name_to_vector(card_name) for card_name in choices],
            [[0] + [1 if choice == choice_dict['picked'] else 0 for choice in choices]]
        ]


if __name__ == '__main__':
    if sys.platform == 'darwin':
        runs_directory = os.path.expanduser(
            '~/Library/Application Support/Steam/steamapps/common/SlayTheSpire/SlayTheSpire.app/Contents/Resources/runs'
        )

        """
    elif sys.platform == 'win32':
        pass
        
    elif sys.platform == 'linux':
        pass
        """

    else:
        raise NotImplementedError

    for character_folder in os.listdir(runs_directory):
        with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder),
                  'w') as training_data_file:
            json.dump([], training_data_file)

        logger.info('Found {number} {character} runs'.format(
            number=len(os.listdir(os.path.join(runs_directory, character_folder))),
            character=character_folder)
        )

        for run_file in os.listdir(os.path.join(runs_directory, character_folder)):
            with open(os.path.join(runs_directory, character_folder, run_file)) as run:
                with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder)) as training_data_file:
                    training_data = json.load(training_data_file)

                run_data = json.load(run)

                relics = [relic['key'] for relic in run_data['relics_obtained']]

                # ignore Question Card and Busted Crown (Molten Egg 2)? runs for now

                if 'Question Card' in relics or 'Molten Egg 2' in relics:
                    continue

                training_data += [choice_dict_to_vectors(choice_dict, relics) for choice_dict in run_data['card_choices']]

                with open('{character_folder}_TRAINING_DATA'.format(character_folder=character_folder), 'w') as training_data_file:
                    json.dump(training_data, training_data_file)
