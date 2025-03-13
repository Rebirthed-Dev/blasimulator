from enum import Enum
from logging import error

from simulator.modules.teams import *

# I would make an actual finite state machine for this but uh
# no
class MatchState(Enum):
    GAME_START = 0
    INNING_START = 1
    INNING_END = 2
    BATTER_UP = 3
    BAT = 4

class Match:
    def __init__(self, home: team.Team, away: team.Team):
        self.stateFunctions = { # maps MatchState Enum to functions in this class
            0: self.state_game_start,
            1: self.state_inning_start,
            2: self.state_inning_end,
            3: self.state_batter_up,
            4: self.state_bat,
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
        self.inningStats.outs = 0
        self.inningStats.batter = 0

        self.bases = [
            [], # batting base
            [], # first base
            [], # second base
            [], # third base
        ]

        self.roundStats = { } # stats for this round (batter), resets whenever a new batter steps up
        self.roundStats.strikes = 0
        self.roundStats.balls = 0

        self.stats = { } # tracks persistent things through the entire game, not just an inning
        self.stats.homeRuns = 0
        self.stats.awayRuns = 0

        self.output = "" # string output for event console

    def get_current_batting_team(self):
        if self.half == 0:
            return self.home
        else:
            return self.away

    def check_if_player_on_base(self, player):
        for base in self.bases:
            if player in base:
                return True
        return False

    def remove_player_from_bases(self, player):
        for base in self.bases:
            if player in base:
                base.remove(player)

    def apply_base_steps(self, current_batter, steps):
        bases_in_play = len(self.bases) - 1
        output_bases = [[] for x in range(0, bases_in_play)]
        batters_scoring = []
        for i, base in enumerate(self.bases):
            target_base = i + steps
            for batter in base:
                if target_base > bases_in_play:
                    batters_scoring.append(batter)
                else:
                    output_bases[target_base].append(batter)

        return output_bases, batters_scoring

    def step(self):
        self.stateFunctions[self.state]()
        return self.output

    def state_game_start (self):
        # do setup and enter initial inning
        self.state = MatchState.INNING_START
        self.inning = 1
        self.half = 0

        # you'd set the output string here or something, then a runner function can grab it before stepping to display
        self.output = "Play Ball!"

    def state_inning_start(self):
        # reset stats
        self.roundStats.strikes = 0
        self.roundStats.balls = 0
        self.inningStats.outs = 0

        if self.half == 0:
            self.inningStats.battingTeam = self.home
        else:
            self.inningStats.battingTeam = self.away

        self.state = MatchState.BATTER_UP

    def state_inning_end(self):
        return

    def state_batter_up(self):
        # get batter
        batting_team = self.get_current_batting_team()
        batters = batting_team.get_lineup()
        batter = None
        if len(batters) == 0:
            # no batters
            # add a batting machine here
            error("NO LINEUP VALID BATTER IN TEAM")
            exit(0)
        elif self.inningStats.batter > len(batters):
            # reset batting lineup
            self.inningStats.batter = 0

        batter = batters[self.inningStats.batter]

        if batter:
            self.remove_player_from_bases(batter)
            self.state = MatchState.BAT
        else:
            error("TRIED TO GET BATTER AND FAILED")
            exit(0)

    def state_bat(self):
        return



