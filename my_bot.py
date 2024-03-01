from poker_game_runner.state import Observation
from poker_game_runner.utils import Range, HandType
import time
import random


class Bot:
    def get_name(self):
        return 'Kevin "bob" Hart'

    def act(self, obs: Observation):
        if obs.current_round == 0:
            return self.pre_flop()
        elif obs.current_round == 1:
            return self.post_flop()
        elif obs.current_round == 2:
            return self.post_turn()
        elif obs.current_round == 3:
            return self.post_river()
        else:
            return 0

        return obs.get_max_raise()  # All-in

    def pre_flop(self):
        pass

    def post_flop(self):
        pass

    def post_turn(self):
        pass

    def post_river(self):
        pass
