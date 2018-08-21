import numpy as np

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

def astar(map_walls):
    maze_dim = len(map_walls)
    h = (maze_dim - 2)*2 # max distance to goal w/o walls
    g = 0 #movement cost

    h_map = np.zeros((maze_dim, maze_dim))
    goal_max = maze_dim/2
    goal_min = maze_dim/2-1
    goal = [[goal_max, goal_min],[goal_min, goal_max], [goal_max,goal_max], [goal_min, goal_min]]

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

    f = g + h
    closed = []
    open = []
    current_path = []
    best_path = ['up']

    location = [11,0]
    parent_node = []

    open_spaces, headings = adjacent([11,0])
    open.append(open_spaces)

    print open_spaces
    print headings

    #TODO code astar loop

    while location not in goal:
        open_spaces = adjacent(location)
        open.append(open_spaces)
        current_path.append(location)
        for i in open:
            # choose smallest f value as next location
            # store heading / current paths
            # check current path against best paths
            #

# create list of adjacent cells to location as list [N,E,S,W]
def adjacent(location):
    adj_spaces = [(location[0]-1, location[1]),     # space to north
    (location[0], location[1]+1),                   # space to east
    (location[0]+1, location[1]),                   # space to south
    (location[0], location[1]-1)]                   # space to west

    print 'init:' + str(adj_spaces)
    maze_dim = len(map_walls)

    # check adj_spaces to see if empty/valid moves order = [N, E, S, W]
    checked_list = []
    heading_list =[]
    j = 0                   # 0 = N, 1 = E, 2 = S, 3 = W
    for i in adj_spaces:
        print 'i:' + str(i)
        print 'j:' + str(j)
        if i[0] > 0 or i[1] > 0:
            if i[0] >= 0 and i[0] < maze_dim:
                if i[1] >= 0 and i[1] < maze_dim:
                    print 'walls:' + str(map_walls[i[0],i[1]])
                    if map_walls[i[0],i[1]] != 0: # check for unexplored
                        if map_walls[i[0],i[1]] not in [1,2,4,8]: #check for dead ends
                            if j == 0:
                                if map_walls[i[0],i[1]] not in [1,2,3,8,9,10,11]: # wall south
                                    checked_list.append(i)
                                    heading_list.append(j)
                            if j == 1:
                                if map_walls[i[0],i[1]] not in [1,2,3,4,5,6,7]: # wall west
                                    checked_list.append(i)
                                    heading_list.append(j)
                            if j == 2:
                                if map_walls[i[0],i[1]] not in [2,4,6,8,10,12,14]: # wall north
                                    checked_list.append(i)
                                    heading_list.append(j)
                            if j == 3:
                                if map_walls[i[0],i[1]] not in [1,4,5,8,9,12,13,]: # wall east
                                    checked_list.append(i)
                                    heading_list.append(j)
        j+=1
    return checked_list, heading_list

astar(map_walls)
