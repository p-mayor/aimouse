import numpy as np
import random
import matplotlib.pyplot as plt


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
        self.rotation = 0
        self.maze_dim = maze_dim

        self.goal_max = self.maze_dim/2
        self.goal_min = self.maze_dim/2-1

        self.map = np.zeros((self.maze_dim, self.maze_dim))
        self.map[maze_dim-1,0] = 1
        self.explo_list = []

        self.map_walls = np.zeros((self.maze_dim, self.maze_dim))
        self.map_walls[maze_dim-1,0] = 1

        self.map_count = np.zeros((self.maze_dim, self.maze_dim))
        self.map_count[maze_dim-1,0] = 0

        self.time_step = 0
        self.run_count = 0

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
            robot self.rotation (if any), as a number: 0 for no self.rotation, +90 for a
            90-degree self.rotation clockwise, and -90 for a 90-degree self.rotation
            counterclockwise. Other values will result in no self.rotation. The second
            value indicates robot self.movement, and the robot will attempt to move the
            number of indicated squares: a positive number indicates forwards
            self.movement, while a negative number indicates backwards self.movement. The
            robot may move a maximum of three units per turn. Any excess self.movement
            is ignored.

            If the robot wants to end a run (e.g. during the first training run in
            the maze) then returing the tuple ('Reset', 'Reset') will indicate to
            the tester to end the run and return the robot to the start.
        '''

        print 'Current Heading: ' + str(self.heading)

        # reset rotation and movement to starting values
        if self.rotation == 'Reset' and self.movement == 'Reset':
            self.rotation = 0
            self.movement = 1

        # random self.rotation variables
        rand_left_straight = random.randrange(-90, 0, 90)
        rand_left_right = random.randrange(-90, 90, 180)
        rand_right_straight = random.randrange(0, 90, 90)
        rand_rotation = random.randrange(-90, 90, 90)

        # exploration map values
        explored_space_value = 1
        current_space_value = 3
        goal_space_value = 2

        # check sensors after move and update self.rotation and bits for wall map
        if self.movement == 1:
            if self.heading == 'up':
                # check 1 way paths
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 1
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 0
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 0
                    self.rotation = 90

                # check 2 way paths and choose random self.rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    self.rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    self.rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    self.rotation = rand_right_straight

                # check 3 way paths and choose random
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    self.rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    self.rotation = 90
                    self.movement = 0

            elif self.heading == 'right':
                # 1 way paths
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 1
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 1
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 1
                    self.rotation = 90

                # check 2 way paths and choose random self.rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    self.rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    self.rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    self.rotation = rand_right_straight

                # check for 3 way paths and choose random self.rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    self.rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    self.rotation = 90
                    self.movement = 0

            elif self.heading == 'down':
                # 1 way paths
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 0
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 0
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 1
                    self.rotation = 90

                # check for 2 way paths and choose random self.rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    self.rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    self.rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 1, 1
                    self.rotation = rand_right_straight

                # check for 3 way paths and choose random self.rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    self.rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    self.rotation = 90
                    self.movement = 0

            elif self.heading == 'left':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 0
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 1
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 0
                    self.rotation = 90

                # check for 2 way paths and choose random self.rotation between the 2
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] == 0: # wall on right
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 1, 1
                    self.rotation = rand_left_straight
                elif sensors[0] > 0 and sensors[1] == 0 and sensors[2] > 0: # wall on front
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 0
                    self.rotation = rand_left_right
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] > 0: # wall on left
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 0, 1
                    self.rotation = rand_right_straight

                # check for 3 way paths and choose random self.rotation
                elif sensors[0] > 0 and sensors[1] > 0 and sensors[2] > 0:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 1, 1, 1
                    self.rotation = rand_rotation

                # check for dead end and rotate +90
                else:
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    self.rotation = 90
                    self.movement = 0

        # check sensors after dead end and 90 self.rotation and update bits
        elif self.movement == 0:
            self.movement = 1
            if self.heading == 'up':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    self.rotation = 90

            elif self.heading == 'right':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 1, 0, 0
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    self.rotation = 90

            elif self.heading == 'down':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    self.rotation = 90

            elif self.heading == 'left':
                if sensors[0] > 0 and sensors[1] == 0 and sensors[2] == 0: # open left only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 1, 0
                    self.rotation = -90
                elif sensors[0] == 0 and sensors[1] > 0 and sensors[2] == 0: # open front only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 0, 0, 0, 1
                    self.rotation = 0
                elif sensors[0] == 0 and sensors[1] == 0 and sensors[2] > 0: # open right only
                    self.top_bit, self.right_bit, self.bot_bit, self.left_bit = 1, 0, 0, 0
                    self.rotation = 90

        # update new location with map_walls bits if not time 0
        if self.time_step != 0:
            self.map_walls[self.location[0], self.location[1]] = (self.top_bit*1 + \
                self.right_bit*2 + self.bot_bit*4 + self.left_bit*8)

        # update heading based on self.rotation
        if self.rotation == -90:
            if self.heading == 'up':
                self.heading = 'left'
            elif self.heading == 'left':
                self.heading = 'down'
            elif self.heading == 'down':
                self.heading = 'right'
            elif self.heading == 'right':
                self.heading = 'up'
        elif self.rotation == 90:
            if self.heading == 'up':
                self.heading = 'right'
            elif self.heading == 'left':
                self.heading = 'up'
            elif self.heading == 'down':
                self.heading = 'left'
            elif self.heading == 'right':
                self.heading = 'down'

        # update map at current location as explored_space_value if not goal
        if self.map[self.location[0], self.location[1]] != 2:
            self.map[self.location[0], self.location[1]] = explored_space_value
            # check for goal area (middle 2x2 square of maze) and set to goal_space_value
            if self.goal_min <= self.location[0] and self.location[0] <= self.goal_max:
                if self.goal_min <= self.location[1] and self.location[1] <= self.goal_max:
                    self.map[self.location[0], self.location[1]] = goal_space_value

        # update counter map with current location
        self.map_count[self.location[0], self.location[1]] += 1

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

        # exploration percentage
        max_map_value = self.maze_dim * self.maze_dim + (goal_space_value*4)-4 + (current_space_value-2)
        current_map_value = np.sum(self.map)
        exploration = (current_map_value / max_map_value)

        # plotting exploration %
        self.explo_list.append(exploration)

        # printouts for testing

        print '{:03d} [{:>2d},{:>2d},{:>2d}] {} {} {}'.format(
            self.time_step,
            sensors[0], sensors[1], sensors[2],
            self.rotation,
            self.movement,
            self.heading)
        print self.map_walls
        print self.map_count
        print self.map

        # time_step update
        self.time_step += 1

        # reset parameters
        if self.time_step == 500:
            plt.plot(self.explo_list)
            plt.show()
            self.rotation = 'Reset'
            self.movement = 'Reset'
            self.heading = 'up'
            self.run_count += 1
            self.location = [self.maze_dim-1, 0]
            self.map = np.zeros((self.maze_dim, self.maze_dim))
            self.map[self.maze_dim-1,0] = 1
            self.top_bit = 1
            self.right_bit = 0
            self.bot_bit = 0
            self.left_bit = 0


        return self.rotation, self.movement
