class Keyboard():

    def __init__(self):
        self.keyboard = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.position = (1, 1)
        self.code = []
        self.movements = {
            'U': (-1, 0),
            'R': (0, 1),
            'D': (1, 0),
            'L': (0, -1),
        }

    def apply_steps(self, steps):
        for step in steps:
            self.apply_step(step)

    def clamp(self, n):
        return max(
            0,
            min(
                len(self.keyboard) - 1,
                n
            )
        )

    def apply_step(self, step):
        for move in list(step):
            x, y = self.position
            movement = self.movements[move]

            self.position = (
                self.clamp(x + movement[0]),
                self.clamp(y + movement[1])
            )

        self.code.append(self.keyboard[self.position[0]][self.position[1]])

    def get_code(self):
        return ''.join(map(str, self.code))