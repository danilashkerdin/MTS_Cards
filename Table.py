from Card import Card
import random


class Table:
    clear_cards: list[Card]
    dropped_cards: list[Card]
    current: Card

    def get_card(self) -> Card:
        if self.is_empty():
            self.shuffle()

        return self.clear_cards.pop()

    def get_cards(self, n: int) -> list[Card]:
        if n <= 0:
            raise Exception("N must be a natural one")

        cards = []
        for i in range(n):
            cards.append(self.get_card())

        return cards

    def drop_card(self, card: Card):
        self.dropped_cards.append(card)

    def is_empty(self) -> bool:
        return len(self.clear_cards) <= 0

    def shuffle(self):
        self.clear_cards += self.dropped_cards
        self.dropped_cards.clear()
        random.shuffle(self.clear_cards)
