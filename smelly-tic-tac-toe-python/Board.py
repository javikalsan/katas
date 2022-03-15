NOT_PLAYED_VALUE = None


class Board(object):
    def __init__(self):
        self._plays_parallel = [NOT_PLAYED_VALUE] * (3 * 3)

    def AddTileAt_parallel(self, symbol, x, y):
        position = self._translate_from_coordinates(x, y)
        self._plays_parallel[position] = symbol

    def _translate_from_coordinates(self, x, y):
        board_map = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}
        return board_map.get(x)[y]

    def TileAt_parallel(self, x, y):
        position = self._translate_from_coordinates(x, y)
        return self._plays_parallel[position] if self._plays_parallel[position] else None
