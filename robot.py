import numpy as np
import random

class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [maze_dim-1, 0]
        self.heading = 'up'
        self.maze_dim = maze_dim
        self.map = np.zeros((self.maze_dim, self.maze_dim))
        self.map[maze_dim-1,0] = 1
        self.time_step = 0
        print self.map

    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        print self.time_step, sensors, self.heading, self.location
        self.time_step += 1
        movement = 1
        # check for 1 way paths
        if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0:
            rotation = -90
            if self.heading == 'up':
                self.heading = 'left'
            if self.heading == 'left':
                self.heading = 'down'
            if self.heading == 'down':
                self.heading = 'right'
            if self.heading == 'right':
                self.heading = 'up'
        if sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0:
            rotation = 0
        if sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0:
            rotation = +90
            if self.heading == 'up':
                self.heading = 'right'
            if self.heading == 'left':
                self.heading = 'up'
            if self.heading == 'down':
                self.heading = 'left'
            if self.heading == 'right':
                self.heading = 'down'
        # check for 3 way paths
        if sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
            rotation =  random.randrange(-90, 90, 90)
            if rotation == -90:
                if self.heading == 'up':
                    self.heading = 'left'
                if self.heading == 'left':
                    self.heading = 'down'
                if self.heading == 'down':
                    self.heading = 'right'
                if self.heading == 'right':
                    self.heading = 'up'
            if rotation == +90:
                if self.heading == 'up':
                    self.heading = 'right'
                if self.heading == 'left':
                    self.heading = 'up'
                if self.heading == 'down':
                    self.heading = 'left'
                if self.heading == 'right':
                    self.heading = 'down'
        # check for 2 way paths
        if sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0:
            rotation = random.randrange(-90, 0, 90)
            if rotation == -90:
                if self.heading == 'up':
                    self.heading = 'left'
                if self.heading == 'left':
                    self.heading = 'down'
                if self.heading == 'down':
                    self.heading = 'right'
                if self.heading == 'right':
                    self.heading = 'up'
            if rotation == +90:
                if self.heading == 'up':
                    self.heading = 'right'
                if self.heading == 'left':
                    self.heading = 'up'
                if self.heading == 'down':
                    self.heading = 'left'
                if self.heading == 'right':
                    self.heading = 'down'
        if sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0:
            rotation = random.randrange(-90, 90, 180)
            if rotation == -90:
                if self.heading == 'up':
                    self.heading = 'left'
                if self.heading == 'left':
                    self.heading = 'down'
                if self.heading == 'down':
                    self.heading = 'right'
                if self.heading == 'right':
                    self.heading = 'up'
            if rotation == +90:
                if self.heading == 'up':
                    self.heading = 'right'
                if self.heading == 'left':
                    self.heading = 'up'
                if self.heading == 'down':
                    self.heading = 'left'
                if self.heading == 'right':
                    self.heading = 'down'
        if sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0:
            rotation = random.randrange(0, 90, 90)
        # check for dead end
        if sensors[0] == 0 and sensors[1] == 0 and sensors[2] == 0:
            rotation = +90
            if self.heading == 'up':
                self.heading = 'right'
            if self.heading == 'left':
                self.heading = 'up'
            if self.heading == 'down':
                self.heading = 'left'
            if self.heading == 'right':
                self.heading = 'down'
        # update location based on heading and movement
        if self.heading == 'up':
            self.location = [self.location[0]-movement, self.location[1]]
        if self.heading == 'left':
            self.location = [self.location[0], self.location[1]-movement]
        if self.heading == 'down':
            self.location = [self.location[0]+movement, self.location[1]]
        if self.heading == 'right':
            self.location = [self.location[0], self.location[1]+movement]



        return rotation, movement
