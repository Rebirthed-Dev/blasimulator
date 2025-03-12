class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def get_name(self):
        return self.name
