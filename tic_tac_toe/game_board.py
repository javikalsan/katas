from typing import List

from entities import Player
from constants import NOT_PLAYED_VALUE


class GameBoard:
    WINNER_COMBINATIONS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self):
        self.grid = [NOT_PLAYED_VALUE] * (3 * 3)

    def update(self, player: Player):
        self.grid[player.position] = player.name

    def is_board_empty(self):
        return len(self.grid) == len([True for position
                                      in self.grid
                                      if position == NOT_PLAYED_VALUE])

    def is_position_used(self, player):
        return self.grid[player.position] != NOT_PLAYED_VALUE

    def is_whole_grid_used(self):
        return NOT_PLAYED_VALUE not in self.grid

    def grid_values_for(self, combination: List) -> List:
        return [self.grid[position] for position in combination]
