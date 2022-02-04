from src.constants import PLAYER_X, PLAYER_O
from src.exceptions import InvalidPositionError, GameOverError
from src.entities import Player, GameStatus
from src.tic_tac_toe import TicTacToe

import unittest


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()

    def test_a_game_has_nine_positions_in_a_3x3_grid(self):

        expected_grid_total_positions = 3 * 3
        self.assertEqual(expected_grid_total_positions, len(self.tic_tac_toe.game_board.grid))

    def test_x_always_goes_first(self):

        self.tic_tac_toe.play(Player(PLAYER_X, 5))

        self.assertEqual(self.tic_tac_toe.game_board.grid[5], PLAYER_X)

    def test_players_alternate_placing_x_and_o_on_the_board(self):

        self.tic_tac_toe.play(Player(PLAYER_X, 5))
        self.tic_tac_toe.play(Player(PLAYER_O, 2))
        self.tic_tac_toe.play(Player(PLAYER_X, 0))

        self.assertEqual(self.tic_tac_toe.game_board.grid[0], PLAYER_X)

    def test_players_cannot_play_on_a_played_position(self):

        self.tic_tac_toe.play(Player(PLAYER_X, 5))
        with self.assertRaises(InvalidPositionError) as context:
            self.tic_tac_toe.play(Player(PLAYER_O, 5))

        self.assertEqual("Invalid position!", str(context.exception))

    def test_player_with_three_x_or_o_in_a_row_wins(self):

        self._tic_tac_toe_play_sequence_x_winner()

        self.assertEqual(PLAYER_X, self.tic_tac_toe.game_status.winner)


    def test_nine_squares_filled_without_winner_game_is_a_draw(self):

        self.tic_tac_toe.play(Player(PLAYER_X, 0))
        self.tic_tac_toe.play(Player(PLAYER_O, 1))
        self.tic_tac_toe.play(Player(PLAYER_X, 2))
        self.tic_tac_toe.play(Player(PLAYER_O, 4))
        self.tic_tac_toe.play(Player(PLAYER_X, 3))
        self.tic_tac_toe.play(Player(PLAYER_O, 6))
        self.tic_tac_toe.play(Player(PLAYER_X, 5))
        self.tic_tac_toe.play(Player(PLAYER_O, 8))
        self.tic_tac_toe.play(Player(PLAYER_X, 7))

        self.assertTrue(self.tic_tac_toe.game_status.draw)

    def test_game_status_is_returned_after_a_turn(self):

        game_status = self.tic_tac_toe.play(Player(PLAYER_X, 0))

        expected_game_status = GameStatus(PLAYER_X, None, False)
        self.assertEqual(game_status, expected_game_status)

    def test_game_over(self):

        self._tic_tac_toe_play_sequence_x_winner()

        with self.assertRaises(GameOverError) as context:
            self.tic_tac_toe.play(Player(PLAYER_O, 3))

        expected_exception_message = str(GameStatus(PLAYER_X, PLAYER_X, False))
        self.assertEqual(expected_exception_message, str(context.exception))

    def _tic_tac_toe_play_sequence_x_winner(self):
        self.tic_tac_toe.play(Player(PLAYER_X, 4))
        self.tic_tac_toe.play(Player(PLAYER_O, 2))
        self.tic_tac_toe.play(Player(PLAYER_X, 8))
        self.tic_tac_toe.play(Player(PLAYER_O, 0))
        self.tic_tac_toe.play(Player(PLAYER_X, 1))
        self.tic_tac_toe.play(Player(PLAYER_O, 5))
        self.tic_tac_toe.play(Player(PLAYER_X, 7))
