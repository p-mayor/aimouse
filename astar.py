import numpy as np


def astar(map_walls, time_step, location):
    maze_dim = len(map_walls)
    h = (maze_dim - 2)*2 # max distance to goal w/o walls
    g = 1 #movement cost
    f = g + h
    closed = []
    open = [location]
    current_path = []
    best_path = []

    h_map = np.zeros((maze_dim, maze_dim))
    goal_max = maze_dim/2
    goal_min = maze_dim/2-1

    # generate heuristic map
    for i in range(len(h_map)):
        for j in range(len(h_map)):
            if i <= goal_min:
                if j <= goal_min:
                    h_map[i][j] = abs(i-goal_min)+abs(j-goal_min)
                elif j > goal_min:
                    h_map[i][j] = abs(i-goal_min)+abs(j-goal_max)
            elif i > goal_min:
                if j <= goal_min:
                    h_map[i][j] = abs(i-goal_max)+abs(j-goal_min)
                elif j > goal_min:
                    h_map[i][j] = abs(i-goal_max)+abs(j-goal_max)

    # create list of adjacent cells to current
    def adj(a):
        list = [(a[0]+1, a[1]),   # space to north
        (a[0], a[1]+1),             # space to east
        (a[0]-1, a[1]),             # space to south
        (a[0], a[1]-1)]             # space to west
        return list

    # check for out of bounds locations
    for i in adj_spaces:
        if i[0] >= 0 and i[0] < (maze_dim-1):
            if i[1] >= 0 and i[1] < (maze_dim-1):
                open.append(i)
                if map_walls[i] == 0: # check for unexplored
                    open.pop(i)
                elif map_walls[i] == 1 or map_walls[i] == 2 or\
                 map_walls[i] == 4 or map_walls[i] == 8: #check for dead ends
                    open.pop(i)

    # create adjacent wall bits
    wall_n, wall_e, wall_s, wall_w = False, False, False, False
    if adj_spaces[0] >= 0 and adj_spaces[0] < (maze_dim-1):
        if map_walls[adj_spaces[0]] >= 0 and map_walls[adj_spaces[0]] < (maze_dim-1):
            if map_walls[adj_spaces[0]] not in [3,5,7,9,15,13]: # wall to north
                wall_n = True
    if adj_spaces[1] >= 0 and adj_spaces[1] < (maze_dim-1):
        if map_walls[adj_spaces[1]] >= 0 and map_walls[adj_spaces[1]] < (maze_dim-1):
            if map_walls[adj_spaces[1]] not in [3,7,15,6,14,10]: # wall to east
                wall_e = True
    if adj_spaces[2] >= 0 and adj_spaces[2] < (maze_dim-1):
        if map_walls[adj_spaces[2]] >= 0 and map_walls[adj_spaces[2]] < (maze_dim-1):
            if map_walls[adj_spaces[2]] not in [5,6,7,12,14,15]: # wall to south
                wall_s = True
    if adj_spaces[3] >= 0 and adj_spaces[3] < (maze_dim-1):
        if map_walls[adj_spaces[3]] >= 0 and map_walls[adj_spaces[3]] < (maze_dim-1):
            if map_walls[adj_spaces[3]] not in [9,10,11,12,14,15]: # wall to west
                wall_w = True

    while len(open) > 0:
        for i in open:
            current_path.append(i)
            closed.append(i)
            if adj(i)
