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
        # time_step update
        self.time_step += 1
        movement = 1

        # check for 1 way paths
        if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0:
            rotation = -90
        if sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0:
            rotation = 0
        if sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0:
            rotation = 90


        # check for 3 way paths and choose random rotation
        if sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
            rotation =  random.randrange(-90, 90, 90)

        # check for 2 way paths and choose random rotation between the 2
        if sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
            rotation = random.randrange(-90, 0, 90)
        if sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
            rotation = random.randrange(-90, 90, 180)
        if sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
            rotation = random.randrange(0, 90, 90)

        # check for dead end and rotate +90
        if sensors[0] == 0 and sensors[1] == 0 and sensors[2] == 0:
            rotation = 90
            movement = 0

        # base move on min between sensor and 3 (max move per step)
        #if rotation == -90:
        #    movement = min(3, sensors[0])
        #elif rotation == 0:
        #    movement = min(3, sensors[1])
        #elif rotation == 90:
        #    movement = min(3, sensors[2])
        #print rotation

        # update heading based on rotation
        if rotation == -90:
            if self.heading == 'up':
                self.heading = 'left'
            elif self.heading == 'left':
                self.heading = 'down'
            elif self.heading == 'down':
                self.heading = 'right'
            elif self.heading == 'right':
                self.heading = 'up'
        elif rotation == 90:
            if self.heading == 'up':
                self.heading = 'right'
            elif self.heading == 'left':
                self.heading = 'up'
            elif self.heading == 'down':
                self.heading = 'left'
            elif self.heading == 'right':
                self.heading = 'down'

        # update location based on heading and movement
        if self.heading == 'up':
            self.location = [self.location[0]-movement, self.location[1]]
        elif self.heading == 'left':
            self.location = [self.location[0], self.location[1]-movement]
        elif self.heading == 'down':
            self.location = [self.location[0]+movement, self.location[1]]
        elif self.heading == 'right':
            self.location = [self.location[0], self.location[1]+movement]

        # update map with explored_space_value
        explored_space_value = 1
        self.map[self.location[0], self.location[1]] = explored_space_value

        # check for goal area (middle 2x2 square of maze) and set to goal_space_value
        goal_space_value = 2
        if (self.maze_dim/2)-1 <= self.location[0] and self.location[0] <= (self.maze_dim/2):
            if (self.maze_dim/2)-1 <= self.location[1] and self.location[1] <= (self.maze_dim/2):
                self.map[self.location[0], self.location[1]] = goal_space_value
        # + 4 from goal spaces

        max_map_value = self.maze_dim * self.maze_dim + (goal_space_value*4)-4
        current_map_value = np.sum(self.map)
        exploration = (current_map_value / max_map_value)*100

        # printouts for testing
        print self.time_step, sensors, self.heading, self.location, self.map, exploration

        return rotation, movement
