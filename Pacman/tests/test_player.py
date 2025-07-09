import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_initial_position(self):
        p = Player(0, 0)
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

    def test_move_right(self):
        p = Player(0, 0)
        p.move("right")
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 0)

    def test_move_up(self):
        p = Player(10, 10)
        p.move("up")
        self.assertEqual(p.y, 5)

if __name__ == '__main__':
    unittest.main()
