# This file contains the decks used for the player and the CPU

import random

DECK_CARDS: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class BlackJackDeck:

    def __init__(self):
        self._deck_cards = DECK_CARDS

    def select_random_card(self) -> int:
        random_index_card = random.randint(0, len(DECK_CARDS)-1)
        return DECK_CARDS[random_index_card]


class PlayerDeck(BlackJackDeck):

    # Main constructor
    def __init__(self):
        super().__init__()
        self._player_deck = [
            super().select_random_card(),
            super().select_random_card()
            ]

    @property
    # READ ONLY #
    def player_deck(self) -> list[int]:
        return self._player_deck

    def add_player_card(self) -> None:
        self._player_deck.append(super().select_random_card())
