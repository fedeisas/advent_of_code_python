import unittest
from navigator import Navigator

class TestNavigator(unittest.TestCase):

    def test_scenario_1(self):
        steps = ['R2', 'L3']

        nav = Navigator()
        nav.apply_steps(steps)

        self.assertEquals(5, nav.get_distance())

    def test_scenario_2(self):
        steps = ['R2', 'R2', 'R2']

        nav = Navigator()
        nav.apply_steps(steps)

        self.assertEquals(2, nav.get_distance())

    def test_scenario_3(self):
        steps = ['R5', 'L5', 'R5', 'R3']

        nav = Navigator()
        nav.apply_steps(steps)

        self.assertEquals(12, nav.get_distance())

    def test_distance_to_duplicate(self):
        steps = ['R8', 'R4', 'R4', 'R8']

        nav = Navigator()
        nav.apply_steps(steps)

        self.assertEquals(4, nav.get_distance_to_first_duplicate())

if __name__ == '__main__':
    unittest.main()