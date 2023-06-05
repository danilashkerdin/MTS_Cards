from Card import Card


class Player:

    cards: list[Card]
    name: str

    def __init__(self, name):
        self.name = name

    def make_move(self):
        pass


class Robot(Player):

    def make_move(self):
        pass

    # случайно брать карту для хода пока валидатор ее не одобрит, потом взять из колоды
