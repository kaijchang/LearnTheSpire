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


"""
Example .run file:

{
    "current_hp_per_floor": [
        67,
        67,
        67,
        67,
        67,
        67,
        61,
        61,
        61,
        13,
        13,
        19,
        19,
        19,
        40,
        10,
        72,
        62,
        50,
        50,
        50,
        50,
        50,
        50,
        50,
        60,
        44,
        36,
        36,
        31,
        26,
        44,
        31,
        60,
        59,
        60,
        48,
        49,
        52,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        58,
        28,
        46,
        21
    ],
    "special_seed": 0,
    "character_chosen": "IRONCLAD",
    "item_purchase_floors": [
        29
    ],
    "floor_reached": 51,
    "gold_per_floor": [
        119,
        119,
        138,
        88,
        13,
        13,
        24,
        24,
        24,
        52,
        52,
        64,
        64,
        64,
        64,
        160,
        160,
        175,
        175,
        175,
        194,
        94,
        94,
        94,
        94,
        176,
        195,
        206,
        4,
        17,
        33,
        33,
        136,
        136,
        149,
        160,
        174,
        229,
        329,
        329,
        381,
        393,
        405,
        435,
        460,
        322,
        353,
        367,
        367,
        367
    ],
    "relics_obtained": [
        {
            "key": "Darkstone Periapt",
            "floor": 9.0
        },
        {
            "key": "Champion Belt",
            "floor": 10.0
        },
        {
            "key": "Pear",
            "floor": 26
        },
        {
            "key": "Charon's Ashes",
            "floor": 38
        },
        {
            "key": "Calipers",
            "floor": 39
        },
        {
            "key": "MawBank",
            "floor": 41
        },
        {
            "key": "Ornamental Fan",
            "floor": 43
        },
        {
            "key": "Frozen Egg 2",
            "floor": 47
        }
    ],
    "is_ascension_mode": false,
    "win_rate": 0,
    "gold": 367,
    "max_hp_per_floor": [
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        72,
        50,
        50,
        50,
        50,
        50,
        50,
        50,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60,
        60
    ],
    "build_version": "2018-11-08",
    "potions_floor_usage": [
        16,
        16,
        33,
        33,
        39,
        39
    ],
    "circlet_count": 0,
    "event_choices": [
        {
            "damage_taken": 0.0,
            "player_choice": "1 cards matched",
            "max_hp_gain": 0.0,
            "gold_loss": 0.0,
            "max_hp_loss": 0.0,
            "event_name": "Match and Keep!",
            "cards_obtained": [
                "Flex"
            ],
            "gold_gain": 0.0,
            "damage_healed": 0.0,
            "floor": 2.0
        },
        {
            "cards_removed": [
                "Defend_R"
            ],
            "player_choice": "Card Removal",
            "damage_taken": 0.0,
            "max_hp_gain": 0.0,
            "gold_loss": 50.0,
            "max_hp_loss": 0.0,
            "event_name": "The Cleric",
            "gold_gain": 0.0,
            "damage_healed": 0.0,
            "floor": 4.0
        },
        {
            "damage_taken": 0.0,
            "player_choice": "Upgraded",
            "cards_upgraded": [
                "Strike_R"
            ],
            "max_hp_gain": 0.0,
            "gold_loss": 0.0,
            "max_hp_loss": 0.0,
            "event_name": "Upgrade Shrine",
            "gold_gain": 0.0,
            "damage_healed": 0.0,
            "floor": 14.0
        },
        {
            "damage_taken": 0,
            "player_choice": "Became a vampire",
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 22,
            "event_name": "Vampires",
            "cards_obtained": [
                "Bite",
                "Bite",
                "Bite",
                "Bite",
                "Bite"
            ],
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 19
        },
        {
            "cards_removed": [
                "Bite"
            ],
            "player_choice": "Elegance",
            "damage_taken": 0,
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 0,
            "event_name": "Back to Basics",
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 20
        },
        {
            "damage_taken": 0,
            "player_choice": "Obtain J.A.X.",
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 0,
            "event_name": "Drug Dealer",
            "cards_obtained": [
                "J.A.X."
            ],
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 23
        },
        {
            "damage_taken": 0,
            "player_choice": "Fight",
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 0,
            "event_name": "Mysterious Sphere",
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 38
        },
        {
            "damage_taken": 0,
            "player_choice": "Fight",
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 0,
            "event_name": "MindBloom",
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 39
        },
        {
            "cards_removed": [
                "Bash"
            ],
            "player_choice": "Removed Attack",
            "damage_taken": 0,
            "max_hp_gain": 0,
            "gold_loss": 0,
            "max_hp_loss": 0,
            "event_name": "Falling",
            "gold_gain": 0,
            "damage_healed": 0,
            "floor": 42
        }
    ],
    "is_prod": false,
    "campfire_rested": 5,
    "neow_bonus": "REMOVE_TWO",
    "score": 727,
    "neow_cost": "TEN_PERCENT_HP_LOSS",
    "campfire_upgraded": 4,
    "chose_seed": false,
    "playtime": 1586,
    "items_purged_floors": [
        5,
        22,
        29,
        46
    ],
    "relics": [
        "Burning Blood",
        "Darkstone Periapt",
        "Champion Belt",
        "Fusion Hammer",
        "Pear",
        "Runic Cube",
        "Charon's Ashes",
        "Calipers",
        "MawBank",
        "Ornamental Fan",
        "Frozen Egg 2"
    ],
    "play_id": "18d1ca6b-4ddb-4c11-8e1a-2ba757aa0aa4",
    "is_endless": false,
    "potions_floor_spawned": [
        3,
        7,
        10,
        12,
        18,
        27,
        31,
        33,
        36,
        37,
        44,
        45,
        48
    ],
    "seed_played": "7189563202095571720",
    "master_deck": [
        "Flex+1",
        "Clash+1",
        "Pummel+1",
        "Offering",
        "Bite",
        "J.A.X.",
        "Clash",
        "Clash+1",
        "Limit Break",
        "Whirlwind",
        "Offering"
    ],
    "is_daily": false,
    "damage_taken": [
        {
            "damage": 11.0,
            "turns": 2.0,
            "enemies": "Jaw Worm",
            "floor": 1.0
        },
        {
            "damage": 6.0,
            "turns": 3.0,
            "enemies": "Cultist",
            "floor": 3.0
        },
        {
            "damage": 12.0,
            "turns": 2.0,
            "enemies": "Small Slimes",
            "floor": 7.0
        },
        {
            "damage": 54.0,
            "turns": 7.0,
            "enemies": "3 Sentries",
            "floor": 10.0
        },
        {
            "damage": 0.0,
            "turns": 3.0,
            "enemies": "Exordium Wildlife",
            "floor": 12.0
        },
        {
            "damage": 36,
            "turns": 5,
            "enemies": "Hexaghost",
            "floor": 16
        },
        {
            "damage": 16,
            "turns": 2,
            "enemies": "Shell Parasite",
            "floor": 18
        },
        {
            "damage": 16,
            "turns": 2,
            "enemies": "2 Thieves",
            "floor": 21
        },
        {
            "damage": 27,
            "turns": 2,
            "enemies": "Snake Plant",
            "floor": 27
        },
        {
            "damage": 22,
            "turns": 2,
            "enemies": "Chosen and Byrds",
            "floor": 28
        },
        {
            "damage": 17,
            "turns": 2,
            "enemies": "Centurion and Healer",
            "floor": 30
        },
        {
            "damage": 15,
            "turns": 2,
            "enemies": "Snake Plant",
            "floor": 31
        },
        {
            "damage": 39,
            "turns": 4,
            "enemies": "Champ",
            "floor": 33
        },
        {
            "damage": 9,
            "turns": 1,
            "enemies": "Orb Walker",
            "floor": 35
        },
        {
            "damage": 9,
            "turns": 1,
            "enemies": "3 Darklings",
            "floor": 36
        },
        {
            "damage": 24,
            "turns": 2,
            "enemies": "Writhing Mass",
            "floor": 37
        },
        {
            "damage": 9,
            "turns": 1,
            "enemies": "2 Orb Walkers",
            "floor": 38
        },
        {
            "damage": 9,
            "turns": 1,
            "enemies": "Mind Bloom Boss Battle",
            "floor": 39
        },
        {
            "damage": 9,
            "turns": 1,
            "enemies": "Spire Growth",
            "floor": 44
        },
        {
            "damage": 18,
            "turns": 5,
            "enemies": "Transient",
            "floor": 45
        },
        {
            "damage": 12,
            "turns": 2,
            "enemies": "Giant Head",
            "floor": 47
        },
        {
            "damage": 36,
            "turns": 1,
            "enemies": "4 Shapes",
            "floor": 48
        },
        {
            "damage": 35,
            "turns": 2,
            "enemies": "Time Eater",
            "floor": 50
        }
    ],
    "campfire_choices": [
        {
            "data": "Flex",
            "key": "SMITH",
            "floor": 6.0
        },
        {
            "data": "Clash",
            "key": "SMITH",
            "floor": 8.0
        },
        {
            "data": "Pummel",
            "key": "SMITH",
            "floor": 11.0
        },
        {
            "data": "Bash",
            "key": "SMITH",
            "floor": 13.0
        },
        {
            "key": "REST",
            "floor": 15.0
        },
        {
            "key": "REST",
            "floor": 25
        },
        {
            "key": "REST",
            "floor": 32
        },
        {
            "key": "REST",
            "floor": 40
        },
        {
            "key": "REST",
            "floor": 49
        }
    ],
    "purchased_purges": 4,
    "is_trial": false,
    "path_per_floor": [
        "M",
        "?",
        "M",
        "?",
        "$",
        "R",
        "M",
        "R",
        "T",
        "E",
        "R",
        "M",
        "R",
        "?",
        "R",
        "B",
        null,
        "M",
        "?",
        "?",
        "M",
        "$",
        "?",
        "$",
        "R",
        "T",
        "M",
        "M",
        "$",
        "M",
        "M",
        "R",
        "B",
        null,
        "M",
        "M",
        "M",
        "?",
        "?",
        "R",
        "T",
        "?",
        "T",
        "M",
        "M",
        "$",
        "E",
        "M",
        "R",
        "B",
        null
    ],
    "victory": true,
    "boss_relics": [
        {
            "picked": "Fusion Hammer",
            "not_picked": [
                "Runic Dome",
                "Orrery"
            ]
        },
        {
            "picked": "Runic Cube",
            "not_picked": [
                "White Beast Statue",
                "Black Star"
            ]
        }
    ],
    "local_time": "20181112175747",
    "items_purged": [
        "Defend_R",
        "Bite",
        "Bite",
        "Bite"
    ],
    "seed_source_timestamp": 0,
    "potions_obtained": [
        {
            "key": "Block Potion",
            "floor": 3.0
        },
        {
            "key": "SkillPotion",
            "floor": 7.0
        },
        {
            "key": "EssenceOfSteel",
            "floor": 10.0
        },
        {
            "key": "Poison Potion",
            "floor": 12.0
        },
        {
            "key": "FearPotion",
            "floor": 18
        },
        {
            "key": "Ancient Potion",
            "floor": 27
        },
        {
            "key": "BloodPotion",
            "floor": 31
        },
        {
            "key": "Swift Potion",
            "floor": 33
        },
        {
            "key": "SteroidPotion",
            "floor": 36
        },
        {
            "key": "Dexterity Potion",
            "floor": 44
        },
        {
            "key": "Explosive Potion",
            "floor": 45
        },
        {
            "key": "AttackPotion",
            "floor": 48
        }
    ],
    "ascension_level": 0,
    "player_experience": 33841,
    "items_purchased": [
        "Regen Potion"
    ],
    "path_taken": [
        "M",
        "?",
        "?",
        "?",
        "?",
        "R",
        "M",
        "R",
        "T",
        "E",
        "R",
        "?",
        "R",
        "?",
        "R",
        "BOSS",
        "M",
        "?",
        "?",
        "M",
        "$",
        "?",
        "$",
        "R",
        "T",
        "M",
        "M",
        "$",
        "?",
        "M",
        "R",
        "BOSS",
        "M",
        "M",
        "?",
        "?",
        "?",
        "R",
        "?",
        "?",
        "T",
        "?",
        "M",
        "$",
        "E",
        "M",
        "R",
        "BOSS"
    ],
    "timestamp": 1542074267,
    "card_choices": [
        {
            "picked": "SKIP",
            "floor": 1.0,
            "not_picked": [
                "Headbutt",
                "Warcry",
                "Wild Strike"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 3.0,
            "not_picked": [
                "Flame Barrier",
                "Rupture",
                "Anger"
            ]
        },
        {
            "picked": "Clash",
            "floor": 7.0,
            "not_picked": [
                "Disarm",
                "True Grit"
            ]
        },
        {
            "picked": "Pummel",
            "floor": 10.0,
            "not_picked": [
                "Pommel Strike",
                "Searing Blow"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 12.0,
            "not_picked": [
                "Carnage",
                "Hemokinesis",
                "Sword Boomerang"
            ]
        },
        {
            "picked": "Offering",
            "floor": 16,
            "not_picked": [
                "Immolate",
                "Berserk"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 18,
            "not_picked": [
                "Armaments",
                "Wild Strike",
                "Corruption"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 21,
            "not_picked": [
                "Headbutt",
                "Reckless Charge+1",
                "Armaments"
            ]
        },
        {
            "picked": "Clash",
            "floor": 27,
            "not_picked": [
                "Shrug It Off",
                "Pommel Strike"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 28,
            "not_picked": [
                "Cleave+1",
                "Body Slam",
                "Warcry"
            ]
        },
        {
            "picked": "Clash+1",
            "floor": 30,
            "not_picked": [
                "Sentinel",
                "Infernal Blade"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 31,
            "not_picked": [
                "Sever Soul",
                "Sword Boomerang",
                "True Grit"
            ]
        },
        {
            "picked": "Limit Break",
            "floor": 33,
            "not_picked": [
                "Bludgeon",
                "Dark Embrace"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 35,
            "not_picked": [
                "Thunderclap",
                "Infernal Blade+1",
                "Wild Strike+1"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 36,
            "not_picked": [
                "Armaments",
                "Inflame+1",
                "Shrug It Off+1"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 37,
            "not_picked": [
                "Intimidate",
                "Sword Boomerang",
                "Wild Strike"
            ]
        },
        {
            "picked": "Whirlwind",
            "floor": 38,
            "not_picked": [
                "Thunderclap",
                "Hemokinesis+1"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 44,
            "not_picked": [
                "Pommel Strike+1",
                "Inflame",
                "Perfected Strike+1"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 45,
            "not_picked": [
                "Feel No Pain+1",
                "Disarm",
                "True Grit+1"
            ]
        },
        {
            "picked": "Offering",
            "floor": 47,
            "not_picked": [
                "Sword Boomerang",
                "Thunderclap"
            ]
        },
        {
            "picked": "SKIP",
            "floor": 48,
            "not_picked": [
                "Pommel Strike",
                "Bloodletting+1",
                "Combust+1"
            ]
        }
    ],
    "is_beta": false
}
"""