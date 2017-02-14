class Navigator:

    def __init__(self):
        self.position = (0, 0)
        self.direction = 0

    def get_position(self):
        return "%d, %d => %s" % (self.position[0], self.position[1], self.position)

    def get_distance(self):
        return sum(map(abs, self.position))

    def get_direction(self):
        directions = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
        return directions[self.direction]

    def turnTo(self, turn):
        if turn == 'R':
            self.direction = (self.direction + 1) % 4
        elif turn == 'L':
            self.direction = (self.direction - 1) % 4

    def move(self, step):
        direction = step[0]
        length = int(step[1:])

        self.turnTo(direction)

        x, y = self.position

        if self.direction == 0:
            self.position = (x, y - length)
        if self.direction == 1:
            self.position = (x + length, y)
        if self.direction == 2:
            self.position = (x, y + length)
        if self.direction == 3:
            self.position = (x - length, y)

    def apply_steps(self, steps):
        for step in steps:
            self.move(step)