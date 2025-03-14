from enum import Enum


class FieldPosition(Enum):
    UNDEFINED = 0
    CATCHER = 1,
    PITCHER = 2,
    FIRST_BASE_GUARD = 3,
    SECOND_BASE_GUARD = 4,
    THIRD_BASE_GUARD = 5,
    LEFT_FIELDER = 6,
    RIGHT_FIELDER = 7,
    CENTER_FIELDER = 8,
    SHORT_STOP = 9

class Player:
    def __init__(self, name, fielding, pitching, batting):
        self.name = name
        self.position = FieldPosition.UNDEFINED
        self.stats = {}
        self.stats.fielding = fielding # 1-10
        self.stats.pitching = pitching # 1-10
        self.stats.batting = batting # 1-10
        # True = Lineup
        self.isLineupOrRotation = False

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats

    def set_lineup(self, lineup):
        self.isLineupOrRotation = lineup