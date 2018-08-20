import numpy as np

def astar(map_walls, time_step, location, heading):
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

# create list of adjacent cells to location as list [N,E,S,W]
def adj(location):
    adj_spaces = [(location[0]+1, location[1]),   # space to north
    (location[0], location[1]+1),             # space to east
    (location[0]-1, location[1]),             # space to south
    (location[0], location[1]-1)]             # space to west

    print 'init' + str(adj_spaces)
    maze_dim = 12

    map_walls = np.array([
        [6,12,4,6,10,10,14,14,10,8,6,12],
        [5,7,13,7,10,10,13,3,14,14,9,5],
        [5,5,5,5,4,6,11,14,9,7,8,5],
        [7,9,3,9,7,11,14,9,6,15,10,9],
        [5,4,6,12,7,10,9,6,13,5,6,12],
        [7,15,13,5,5,6,14,13,7,13,5,5],
        [5,5,7,13,5,3,9,3,13,7,9,5],
        [5,7,9,3,15,10,12,2,15,9,2,13],
        [5,3,10,12,3,14,11,12,7,10,10,13],
        [7,14,10,13,6,15,0,5,1,6,12,5],
        [5,5,6,9,5,5,7,13,4,5,5,5],
        [1,3,11,10,9,3,9,3,11,11,11,9],
    ])

    # check adj_spaces to see if empty/valid moves order = [N, E, S, W]
    checked_list = []
    j = 0
    for i in adj_spaces:
        print i
        print j
        if i[0] > 0 or i[1] > 0:
            if i[0] >= 0 and i[0] < (maze_dim):
                if i[1] >= 0 and i[1] < (maze_dim):
                    print map_walls[i[0],i[1]]
                    if map_walls[i[0],i[1]] != 0: # check for unexplored
                        if map_walls[i[0],i[1]] not in [1,2,4,8]: #check for dead ends
                            if j == 0:
                                if map_walls[i[0],i[1]] not in [5,6,7,12,14,15]: # wall south
                                    checked_list.append(i)
                            if j == 1:
                                if map_walls[i[0],i[1]] not in [9,10,11,12,14,15]: # wall west
                                    checked_list.append(i)
                            if j == 2:
                                if map_walls[i[0],i[1]] not in [3,5,7,9,15,13]: # wall north
                                    checked_list.append(i)
                            if j == 3:
                                if map_walls[i[0],i[1]] not in [3,7,15,6,14,10]: # wall east
                                    checked_list.append(i)
        j+=1
    return checked_list

print adj([11,0])
