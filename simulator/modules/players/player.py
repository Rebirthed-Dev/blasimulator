class Player:
    def __init__(self, name, fielding, pitching, batting):
        self.name = name
        self.stats = {}
        self.stats.fielding = fielding # 1-10
        self.stats.pitching = pitching # 1-10
        self.stats.batting = batting # 1-10

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats