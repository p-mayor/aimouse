

def astar(map_walls):
    maze_dim = 12
    h = (maze_dim - 2)*2 # max distance to goal w/o walls
    g = 10 #movement cost
    f = g + h
    closed = []
    open = []
    current_path = []
    best_path = []
    f_map = np.zeros((maze_dim, maze_dim))
    goal_max = maze_dim/2
    goal_min = maze_dim/2-1

    for i in f_map:
        f_map[i] = float('inf')

    f_map[location[0], location[1]] = min(abs(location[0]-goal_max))

    closed.append(location)

    check_list = [(location[0]+1, location[1]),   # space to north
        (location[0], location[1]+1),             # space to east
        (location[0]-1, location[1]),             # space to south
        (location[0], location[1]-1)]             # space to west

    # check for out of bounds locations
    for i in check_list:
        if i[0] >= 0 and i[0] < (maze_dim-1):
            if i[1] >= 0 and i[1] < (maze_dim-1):
                open.append(i)
                if map_walls[i] == 0: # check for unexplored
                    open.pop(i)
                elif map_walls[i] == 1 or map_walls[i] == 2 or map_walls[i] == 4 or map_walls[i] == 8: #check for dead ends
                    open.pop(i)


    wall_n, wall_e, wall_s, wall_w = False, False, False, False

    if map_walls[check_list[0]] not in [3,5,7,9,15,13]: # wall to north
        wall_n = True
    if map_walls[check_list[1]] not in [3,7,15,6,14,10]: # wall to east
        wall_e = True
    if map_walls[check_list[2]] not in [5,6,7,12,14,15] # wall to south
        wall_s = True
    if map_walls[check_list[3]] not in [9,10,11,12,14,15]: # wall to west
        wall_w = True

    for i in open:
        
