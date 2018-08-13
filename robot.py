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
        self.map_walls = np.zeros((self.maze_dim, self.maze_dim))
        self.map_walls[maze_dim-1,0] = 1
        self.time_step = 0

        # bits for mapping walls (start is always 1)
        self.top_bit = 1
        self.right_bit = 0
        self.bot_bit = 0
        self.left_bit = 0
        self.movement = 1


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
            value indicates robot self.movement, and the robot will attempt to move the
            number of indicated squares: a positive number indicates forwards
            self.movement, while a negative number indicates backwards self.movement. The
            robot may move a maximum of three units per turn. Any excess self.movement
            is ignored.

            If the robot wants to end a run (e.g. during the first training run in
            the maze) then returing the tuple ('Reset', 'Reset') will indicate to
            the tester to end the run and return the robot to the start.
        '''

        # random rotation variables
        rand_left_straight = random.randrange(-90, 0, 90)
        rand_left_right = random.randrange(-90, 90, 180)
        rand_right_straight = random.randrange(0, 90, 90)
        rand_rotation = random.randrange(-90, 90, 90)

        # check sensors after move
        if self.movement == 1:
            if self.heading == 'up':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 1
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 0
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 0
                    rotation = 90

                # check for 2 way paths and choose random rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    rotation = rand_right_straight

                # check for 3 way paths and choose random rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    rotation = 90
                    self.movement = 0

            elif self.heading == 'right':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 1
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 1
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 1
                    rotation = 90

                # check for 2 way paths and choose random rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    rotation = rand_right_straight

                # check for 3 way paths and choose random rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    rotation = 90
                    self.movement = 0

            elif self.heading == 'down':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 1
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 0
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 1
                    rotation = 90

                # check for 2 way paths and choose random rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    rotation = rand_right_straight

                # check for 3 way paths and choose random rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    rotation = 90
                    self.movement = 0

            elif self.heading == 'left':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 0
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 1
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 0
                    rotation = 90

                # check for 2 way paths and choose random rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    rotation = rand_right_straight

                # check for 3 way paths and choose random rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    rotation = 90
                    self.movement = 0

        # check sensors after dead end and 90 rotation
        elif self.movement == 0:
            self.movement = 1
            if self.heading == 'up':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    rotation = 90

            elif self.heading == 'right':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    rotation = 90

            elif self.heading == 'down':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    rotation = 90

            elif self.heading == 'left':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    rotation = 90

        # update new location with map_walls bits if not time 0
        if self.time_step != 0:
            self.map_walls[self.location[0], self.location[1]] = (self.top_bit*1 + \
                self.right_bit*2 + self.bot_bit*4 + self.left_bit*8)

        # base move on min between sensor and 3 (max move per step)
        #if rotation == -90:
        #    self.movement = min(3, sensors[0])
        #elif rotation == 0:
        #    self.movement = min(3, sensors[1])
        #elif rotation == 90:
        #    self.movement = min(3, sensors[2])
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

        # exploration map values
        explored_space_value = 1
        current_space_value = 3
        goal_space_value = 2

        # update map at current location as explored_space_value if not goal
        if self.map[self.location[0], self.location[1]] != 2:
            self.map[self.location[0], self.location[1]] = explored_space_value

        # update location based on heading and self.movement
        if self.heading == 'up':
            self.location = [self.location[0]-self.movement, self.location[1]]
        elif self.heading == 'left':
            self.location = [self.location[0], self.location[1]-self.movement]
        elif self.heading == 'down':
            self.location = [self.location[0]+self.movement, self.location[1]]
        elif self.heading == 'right':
            self.location = [self.location[0], self.location[1]+self.movement]

        # update map at new location as current_space_value
        self.map[self.location[0], self.location[1]] = current_space_value

        # check for goal area (middle 2x2 square of maze) and set to goal_space_value

        if (self.maze_dim/2)-1 <= self.location[0] and self.location[0] <= (self.maze_dim/2):
            if (self.maze_dim/2)-1 <= self.location[1] and self.location[1] <= (self.maze_dim/2):
                self.map[self.location[0], self.location[1]] = goal_space_value

        # exploration percentage
        max_map_value = self.maze_dim * self.maze_dim + (goal_space_value*4)-4 + (current_space_value-2)
        current_map_value = np.sum(self.map)
        exploration = (current_map_value / max_map_value)

        # printouts for testing
        print 'Time Step: ' + str(self.time_step), 'Sensors: ' + str(sensors),\
            'Heading: ' + str(self.heading), 'Location: ' + str(self.location),\
            'Exploration: ' + '{:2.2%}'.format(exploration), '\n', self.map, '\n', self.map_walls,\
            self.top_bit, self.right_bit, self.bot_bit, self.left_bit

        # time_step update
        self.time_step += 1

        return rotation, self.movement
