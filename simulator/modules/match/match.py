from enum import Enum
from simulator.modules.teams import *

# I would make an actual finite state machine for this but uh
# no
class MatchState(Enum):
    GAME_START = 0
    INNING_START = 1
    INNING_END = 2
    GAME_END = 3
    LINEUP_BAT = 3

class Match:
    def __init__(self, home: team.Team, away: team.Team):
        self.stateFunctions = { # maps MatchState Enum to functions in this class
            0: self.state_game_start,
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
        }
        self.seed = 0 # number gen seed, must be consistent so match is reproducible
        self.state = MatchState.GAME_START
        self.home = home
        self.away = away
        self.inning = 1
        self.half = 0

        self.inningStats = { } # stats for this inning, reset every time an inning starts
        self.inningStats.strikes = 0
        self.inningStats.balls = 0

        self.stats = { } # tracks persistent things through the entire game, not just an inning
        self.stats.homeRuns = 0
        self.stats.awayRuns = 0

        self.output = "" # string output for event console

    def step(self):
        self.stateFunctions[self.state]()

    def state_game_start (self):
        # do setup and enter initial inning
        self.state = MatchState.INNING_START

        # you'd set the output string here or something, then a runner function can grab it before stepping to display
        self.output = "Play Ball!"


