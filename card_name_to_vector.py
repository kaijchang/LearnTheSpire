import json
import re

with open('CARDS.json') as cards_file:
    cards = json.load(cards_file)


def clean_text(text):
    return re.sub(r'[.,()]', '', text).casefold()


def get_vocab():
    words = map(
        lambda card:
        list(map(clean_text, card['Description'].split())) +
        list(map(clean_text, card['Description (Upgraded)'].split())), cards)

    flattened_words = [word for sublist in words for word in sublist]

    return set(flattened_words)


def card_name_to_vectors(card_name):
    upgraded = False

    if card_name[-2:] == '+1':
        card_name = card_name[:-2]
        upgraded = True

    card = next(filter(lambda card: card_name.casefold() == card['Name'].casefold(), cards))
    card_text = list(map(clean_text, card['Description (Upgraded)'] if upgraded else card['Description'].split()))

    return card['Cost'], [card_text.count(word) for word in get_vocab()]
