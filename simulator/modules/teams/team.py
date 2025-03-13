from simulator.modules.players.player import Player


class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_name(self):
        return self.name

    def get_lineup(self):
        return [x for x in self.players if x.isLineupOrRotation]
