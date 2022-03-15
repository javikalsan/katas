from Board import Board


class Game(object):
    ROWS = [0, 1, 2]
    NOT_PLAYED_VALUE = None
    PLAYER_O = 'O'

    def __init__(self):
        self._lastSymbol = self.NOT_PLAYED_VALUE
        self._board = Board()

    def play(self, symbol, x, y):
        self._apply_validations(symbol, x, y)
        self._update_game_state(symbol, x, y)

    def winner(self):
        for row in self.ROWS:
            if self._is_empty_row(row):
                continue
            if self._is_three_in_a_row(row):
                return self._board.player_at_position(row, 0)
        return self.NOT_PLAYED_VALUE

    def _apply_validations(self, symbol, x, y):
        if self._is_first_move() and self._is_O_player_turn(symbol):
            raise Exception('Invalid first player')
        if self._is_player_repeated(symbol):
            raise Exception('Invalid next player')
        if self._is_tile_used(x, y):
            raise Exception('Invalid position')

    def _update_game_state(self, symbol, x, y):
        self._lastSymbol = symbol
        self._board.insert_player_at_position(symbol, x, y)

    def _is_first_move(self):
        return self._lastSymbol == self.NOT_PLAYED_VALUE

    def _is_O_player_turn(self, symbol):
        return symbol == self.PLAYER_O

    def _is_player_repeated(self, symbol):
        return symbol == self._lastSymbol

    def _is_tile_used(self, x, y):
        return self._board.player_at_position(x, y) != self.NOT_PLAYED_VALUE

    def _is_three_in_a_row(self, row):
        return self._board.player_at_position(row, 0) == self._board.player_at_position(row, 1) \
               and self._board.player_at_position(row, 2) == self._board.player_at_position(row, 1)

    def _is_empty_row(self, row):
        if self._board.player_at_position(row, 0) == self.NOT_PLAYED_VALUE \
                and self._board.player_at_position(row, 1) == self.NOT_PLAYED_VALUE \
                and self._board.player_at_position(row, 2) == self.NOT_PLAYED_VALUE:
            return True
        return False
