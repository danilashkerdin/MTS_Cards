from Card import Card, SpecialCard, ColoredCard, Color, Digit, SpecialAction, Action
import random


class Table:
    clear_cards: list[Card]
    dropped_cards: list[Card]
    current: Card

    def __init__(self):
        self.clear_cards = [ColoredCard(x, y) for x in Color for y in Digit] + \
                           [ColoredCard(x, y) for x in Color for y in Digit if y != 0] + \
                           2 * [ColoredCard(x, y) for x in Color for y in Action] + \
                           [SpecialCard(x) for x in SpecialAction]
        self.current = self.get_card()
        self.dropped_cards = [self.current]

    def get_card(self) -> Card:
        if self.is_empty:
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

    @property
    def is_empty(self) -> bool:
        return len(self.clear_cards) <= 0

    def shuffle(self):
        self.clear_cards += self.dropped_cards
        self.dropped_cards.clear()
        random.shuffle(self.clear_cards)

    def validate(self):
        # some check of current_card + dropped_card[-1]
        pass


a = [ColoredCard(x, y) for x in Color for y in Digit if y != 0]
for i in a:
    print(i.value, i.color)
