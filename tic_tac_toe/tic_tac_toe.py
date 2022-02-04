from constants import NOT_PLAYED_VALUE, PLAYER_O
from entities import Player, GameStatus
from exceptions import InvalidPositionError, InvalidTurnError, GameOverError
from game_board import GameBoard


class TicTacToe:
    def __init__(self):
        self.game_board = GameBoard()
        self.game_status = GameStatus(None, None, False)

    def play(self, player: Player) -> GameStatus:
        self._run_validations(player)
        self._run_current_turn(player)
        self._handle_game_status()
        return self.game_status

    def _handle_game_status(self):
        self._check_if_there_is_a_winner()
        self._check_if_is_a_draw()

    def _run_current_turn(self, player: Player):
        self.game_board.update(player)
        self.game_status = GameStatus(last_player=player.name,
                                      winner=None,
                                      draw=False)

    def _run_validations(self, player: Player):
        self._raise_error_if_game_is_over()
        self._raise_error_if_x_is_not_the_first_player(player)
        self._raise_error_if_players_are_not_alternating(player)
        self._raise_error_if_position_is_used(player)

    def _raise_error_if_game_is_over(self):
        if self.game_status.winner is not None:
            raise GameOverError(str(self.game_status))

    def _raise_error_if_x_is_not_the_first_player(self, player: Player):
        if self.game_board.is_board_empty() and player.name == PLAYER_O:
            raise InvalidTurnError("It's not your turn!")

    def _raise_error_if_players_are_not_alternating(self, player: Player):
        if player.name == self.game_status.last_player:
            raise InvalidTurnError("It's not your turn!")

    def _raise_error_if_position_is_used(self, player: Player):
        if self.game_board.is_position_used(player):
            raise InvalidPositionError("Invalid position!")

    def _check_if_there_is_a_winner(self):
        for winner_combination in self.game_board.WINNER_COMBINATIONS:
            winner_combination_values = self.game_board.grid_values_for(winner_combination)
            self._update_game_status_if_there_is_a_winner(winner_combination_values)

    def _update_game_status_if_there_is_a_winner(self, winner_combination_values):
        if self._all_values_are_the_same_for(winner_combination_values) \
                and NOT_PLAYED_VALUE not in winner_combination_values:
            self.game_status = GameStatus(last_player=self.game_status.last_player,
                                          winner=winner_combination_values[0],
                                          draw=self.game_status.draw)

    def _all_values_are_the_same_for(self, winner_combination_values):
        return all(first_value == winner_combination_values[0]
                   for first_value
                   in winner_combination_values)

    def _check_if_is_a_draw(self):
        if self.game_board.is_whole_grid_used():
            self.game_status = GameStatus(last_player=self.game_status.last_player,
                                          winner=self.game_status.winner,
                                          draw=True)
