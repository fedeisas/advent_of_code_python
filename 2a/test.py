import unittest
from keyboard import Keyboard

class TestKeyboard(unittest.TestCase):

    def test_scenario_1(self):
        steps = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD',
        ]

        keyboard = Keyboard()
        keyboard.apply_steps(steps)

        self.assertEquals('1985', keyboard.get_code())

if __name__ == '__main__':
    unittest.main()
