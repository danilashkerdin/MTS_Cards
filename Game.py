from collections import deque

from Player import Player, Robot
from Table import Table


class MTSGame:

    def __init__(self, main_player_name: str, players_count: int):
        self.table = Table()
        self.main_player_name = main_player_name
        self.players_count = players_count

    @property
    def players(self) -> deque[Player | Robot]:
        return deque([Player(name=self.main_player_name)] + [Robot() for _ in range(self.players_count - 1)])

    def start(self):
        for player in self.players:
            player.cards = self.table.get_cards(7)
        while True:
            self.players[0].make_move()
            if self.players[0].won:
                break
            self.players.rotate(1)

    def finish(self):
        pass
