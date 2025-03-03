# This file contains the decks used for the player and the CPU

import random

DECK_CARDS: int = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class DeckBlackJack:

    def __init__(self):
        self.deck_cards = DECK_CARDS
        

    def add_card_to_given_deck(deck: list[int], card: int) -> list[int]:
        return deck.append(card)


    def select_random_card_from_deck() -> int:
        random_index_card = random.randint(0, len(DECK_CARDS))
        return DECK_CARDS[random_index_card]

class DeckPlayer(DeckBlackJack):
    pass
# deck_player: int = []
# deck_cpu: int = []

# Functions to manipulate data


