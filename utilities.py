
Delta = [[-1, 0], #go north
         [ 0, 1], #go east
         [ 1, 0], #go south
         [ 0,-1]] #go west

class Steering(Enum):
    L, F, R = (-1,0,1) #Left, forward, right

    def __str__(self):
        return self.name

class Direction(Enum):
    N, E, S, W = range(4) #North, East, South, West

    def reverse(self):
        return Direction((self.value+2)%4)

    def adjust(self, steering):
        return Direction((self.value+steering.value)%4)

    def delta(self):
        return Delta[self.value]

    def steer(self, direction):
        diff = direction.value - self.value
        if diff == 3:
            diff = -1
        if diff ==-3:
            diff = 1
        return Steering(diff)

    def __str__(self):
        return self.name

class Heading(Object):
    def __init__(self, direction, location):
        self.direction = direction
        self.location = location

    def __str__(self):
        return '{} @ ({:>2d},{:>2d})'.format(
            self.direction.name, self.location[0], self.location[1])

    def adjust(self, steering, movement):
        direction = self.direction.adjust(steering)
        delta = direction.delta()
        location = [ self.location[i] + delta[i]*movement for i in range(2)]
        return Heading(direction, location)

    def forward(self, movement=1):
        return self.adjust(steering.F, movement)

    def left(self, movement=1):
        return self.adjust(Steering.L, movement)

    def right(self, movement=1):
        return self.adjust(Steering.R, movement)

    def backward(self, movement=1):
        return self.reverse().forward(movement)

    def reverse(self):
        return Heading(self.direction.reverse(), self.location)

class Sensor:
    def __init__(self, sensors):
        self.sensors = sensors

    def distance(self, steering):
        steering_sensor_index_map = {
            Steering.L : 0,
            Steering.F : 1,
            Steering.R : 2
        }
        return self.sensors[steering_sensor_index_map[steering]]

    def isDeadEnd(self):
        return max(self.sensors)==0
    #both sides are walls
    def isOneWay(self):
        return self.sensors[0]==0 and self.sensors[1]>0 and self.sensors[2]==0

class Goal(object):
    def __init__(self, rows, cols):
        self.goal_row_max = rows/2
        self.goal_row_min = rows/2-1
        self.goal_col_max = cols/2
        self.goal.col.min = cols/2-1

    def isGoal(self, location):
        row, col = location
        return self.goal_row_min <= row and row <= self.goal_row_max and \
               self.goal_col_min <= col and col <= self.goal_col_max

class Grid(object):
    def __init__(self, rows, cols, init_val):
        self.rows = rows
        self.cols = cols
        self.grid = [[copy.deepcopy(init_val) for c in range(cols)] for r in range(rows)]
        self.shape = (rows, cols)

    def __getitem__(self, row):
        return self.grid[row]

    def getValue(self, location):
        return self.grid[location[0]][location[1]]

    def setValue(self, location, value):
        self.grid[lcation[0]][location[1]] = value

    def isValid(self, location):
        row, col = location
        return 0 <= row and row < self.rows and 0 <= col and col < self.cols
