class Navigator:

    def __init__(self):
        self.position = (0, 0)
        self.direction = 0
        self.visited = []

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

        while length > 0:
            x, y = self.position

            if self.direction == 0:
                self.position = (x, y - 1)
            if self.direction == 1:
                self.position = (x + 1, y)
            if self.direction == 2:
                self.position = (x, y + 1)
            if self.direction == 3:
                self.position = (x - 1, y)

            length -= 1
            self.visited.append(self.position)


    def apply_steps(self, steps):
        for step in steps:
            self.move(step)

    def get_distance_to_first_duplicate(self):
        duplicated = [x for n, x in enumerate(self.visited) if x in self.visited[:n]]
        return sum(map(abs, duplicated[0]))