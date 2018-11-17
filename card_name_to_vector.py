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

    return list(sorted(set(flattened_words)))


def get_card(card_name, upgraded=False):
    card = next(filter(lambda card: card_name.casefold() == card['Name'].casefold(), cards))

    cost = card['Cost'] if type(card['Cost']) == int else (
        int(re.sub(r'[()]', '', card['Cost']).split()[1]) if upgraded else
        int(re.sub(r'[()]', '', card['Cost']).split()[0]))

    if upgraded and card['Description (Upgraded)']:
        text = card['Description (Upgraded)']

    else:
        text = card['Description']

        match = re.search(r'[0-9]+ \([0-9]+\)', text)

        while match:
            text = text[:match.start()] + \
                   (re.sub(r'[()]', '', match.group(0)).split()[1] if upgraded else \
                   re.sub(r'[()]', '', match.group(0)).split()[0]) + text[match.end():]
            match = re.search(r'[0-9]+ \([0-9]+\)', text)

    return cost, text


def card_name_to_vector(card_name):
    upgraded = False

    if card_name[-2:] == '+1':
        card_name = card_name[:-2]
        upgraded = True

    cost, text = get_card(card_name, upgraded)

    return [[cost] + [text.split().count(word) for word in get_vocab()]]
