import sys
import unittest
from trivia.game import execute

class TestGame(unittest.TestCase):
    def test_golden_master(self):
        with open('./tests/current_game.output', 'w') as sys.stdout:
            execute()

        with open('./tests/current_game.output', 'r') as file:
            current_output = file.read()

        with open('./tests/golden_master.output', 'r') as file:
            expected_output = file.read()

        self.assertTrue(current_output == expected_output)
