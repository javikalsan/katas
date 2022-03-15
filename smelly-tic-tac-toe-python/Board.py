class Board(object):
    NOT_PLAYED_VALUE = None
    BOARD_MAP = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}

    def __init__(self):
        self._plays_parallel = [self.NOT_PLAYED_VALUE] * (3 * 3)

    def insert_player_at_position(self, symbol, x, y):
        position = self._translate_from_coordinates(x, y)
        self._plays_parallel[position] = symbol

    def player_at_position(self, x, y):
        position = self._translate_from_coordinates(x, y)
        return self._plays_parallel[position] if self._plays_parallel[position] else None

    def _translate_from_coordinates(self, x, y):
        return self.BOARD_MAP.get(x)[y]
