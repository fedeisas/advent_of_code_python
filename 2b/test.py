import unittest
from keyboard import FancyKeyboard

class TestFancyKeyboard(unittest.TestCase):

    def test_scenario_1(self):
        steps = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD',
        ]

        keyboard = FancyKeyboard()
        keyboard.apply_steps(steps)

        self.assertEquals('5DB3', keyboard.get_code())

if __name__ == '__main__':
    unittest.main()
