from Board import Board


class Game(object):
    ROWS = [0, 1, 2]
    EMPTY = ' '
    PLAYER_O = 'O'

    def __init__(self):
        self._lastSymbol = self.EMPTY
        self._board = Board()

    def play(self, symbol, x, y):
        self._apply_validations(symbol, x, y)
        self._update_game_state(symbol, x, y)

    def winner(self):
        for row in self.ROWS:
            if self._is_empty_row(row):
                continue
            if self._is_three_in_a_row(row):
                return self._board.TileAt(row, 0).Symbol
        return self.EMPTY

    def _apply_validations(self, symbol, x, y):
        if self._is_first_move() and self._is_O_player_turn(symbol):
            raise Exception('Invalid first player')
        if self._is_player_repeated(symbol):
            raise Exception('Invalid next player')
        if self._is_tile_used(x, y):
            raise Exception('Invalid position')

    def _update_game_state(self, symbol, x, y):
        self._lastSymbol = symbol
        self._board.AddTileAt(symbol, x, y)

    def _is_first_move(self):
        return self._lastSymbol == self.EMPTY

    def _is_O_player_turn(self, symbol):
        return symbol == self.PLAYER_O

    def _is_player_repeated(self, symbol):
        return symbol == self._lastSymbol

    def _is_tile_used(self, x, y):
        return self._board.TileAt(x, y).Symbol != self.EMPTY

    def _is_three_in_a_row(self, row):
        return self._board.TileAt(row, 0).Symbol == self._board.TileAt(row, 1).Symbol \
                and self._board.TileAt(row, 2).Symbol == self._board.TileAt(row, 1).Symbol

    def _is_empty_row(self, row):
        if self._board.TileAt(row, 0).Symbol == self.EMPTY \
                and self._board.TileAt(row, 1).Symbol == self.EMPTY \
                and self._board.TileAt(row, 2).Symbol == self.EMPTY:
            return True
        return False
