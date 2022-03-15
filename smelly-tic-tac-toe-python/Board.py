from Tile import Tile


NOT_PLAYED_VALUE = ''


class Board(object):
    def __init__(self):
        self._plays_parallel = [NOT_PLAYED_VALUE] * (3 * 3)
        self._plays = []
        for i in range(3):
            for j in range(3):
                tile = Tile()
                tile.X = i
                tile.Y = j
                tile.Symbol = ' '
                self._plays.append(tile)

    def AddTileAt_parallel(self, symbol, x, y):
        position = self._translate_from_coordinates(x, y)
        self._plays_parallel[position] = symbol

    def _translate_from_coordinates(self, x, y):
        board_map = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}
        return board_map.get(x)[y]

    def AddTileAt(self, symbol, x, y):
        new_tile = Tile()
        new_tile.X = x
        new_tile.Y = y
        new_tile.Symbol = symbol

        self.TileAt(x, y).Symbol = symbol

    def TileAt_parallel(self, x, y):
        position = self._translate_from_coordinates(x, y)
        return self._plays_parallel[position]

    def TileAt(self, x, y):
        for t in self._plays:
            if t.X == x and t.Y == y:
                return t
        return None
