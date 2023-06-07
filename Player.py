import time

from Card import Card


class Player:

    cards: list[Card]
    name: str
    won: bool = False

    def __init__(self, name):
        self.name = name

    @property
    def iter_cards(self):
        return iter(self.cards)

    def make_move(self, card: Card):
        pass


class Robot(Player):
    name = "Bot"
    counter = 0
    delay = 5  # seconds

    def __init__(self):
        Robot.counter += 1
        super().__init__(f"{self.name}{Robot.counter}")

    def make_move(self, card: Card = None):
        time.sleep(self.delay)
        return next(self.iter_cards)

    # случайно брать карту для хода пока валидатор ее не одобрит, потом взять из колоды

