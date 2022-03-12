from Board import Board


class Game(object):

    def __init__(self):
        self._lastSymbol = ' '
        self._board = Board()

    def play(self, symbol, x, y):
        if self._is_first_move() and self._is_O_player_turn(symbol):
            raise Exception('Invalid first player')

        if self._is_player_repeated(symbol):
            raise Exception('Invalid next player')

        if self._is_tile_used(x, y):
            raise Exception('Invalid position')

        # update game state
        self._lastSymbol = symbol
        self._board.AddTileAt(symbol, x, y)

    def _is_first_move(self):
        return self._lastSymbol == ' '

    def _is_O_player_turn(self, symbol):
        return symbol == 'O'

    def _is_player_repeated(self, symbol):
        return symbol == self._lastSymbol

    def _is_tile_used(self, x, y):
        return self._board.TileAt(x, y).Symbol != ' '

    def winner(self):
        # if the positions in first row are taken
        if self._board.TileAt(0, 0).Symbol != ' ' \
                and self._board.TileAt(0, 1).Symbol != ' ' \
                and self._board.TileAt(0, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.TileAt(0, 0).Symbol == self._board.TileAt(0, 1).Symbol \
                    and self._board.TileAt(0, 2).Symbol == self._board.TileAt(0, 1).Symbol:
                return self._board.TileAt(0, 0).Symbol

        # if the positions in first row are taken
        if self._board.TileAt(1, 0).Symbol != ' ' \
                and self._board.TileAt(1, 1).Symbol != ' ' \
                and self._board.TileAt(1, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.TileAt(1, 0).Symbol == self._board.TileAt(1, 1).Symbol \
                    and self._board.TileAt(1, 2).Symbol == self._board.TileAt(1, 1).Symbol:
                return self._board.TileAt(1, 0).Symbol

        # if the positions in first row are taken
        if self._board.TileAt(2, 0).Symbol != ' ' \
                and self._board.TileAt(2, 1).Symbol != ' ' \
                and self._board.TileAt(2, 2).Symbol != ' ':
            # if first row is full with same symbol
            if self._board.TileAt(2, 0).Symbol == self._board.TileAt(2, 1).Symbol \
                    and self._board.TileAt(2, 2).Symbol == self._board.TileAt(2, 1).Symbol:
                return self._board.TileAt(2, 0).Symbol

        return ' '
