import numpy as np

maze_01 = np.array([
    [1,5,7,5,5,5,7,5,7,5,5,6],
    [3,5,14,3,7,5,15,4,9,5,7,12],
    [11,6,10,10,9,7,13,6,3,5,13,4],
    [10,9,13,12,3,13,5,12,9,5,7,6],
    [9,5,6,3,15,5,5,7,7,4,10,10],
    [3,5,15,14,10,3,6,10,11,6,10,10],
    [9,7,12,11,12,9,14,9,14,11,13,14],
    [3,13,5,12,2,3,13,6,9,14,3,14],
    [11,4,1,7,15,13,7,13,6,9,14,10],
    [11,5,6,10,9,7,13,5,15,7,14,8],
    [11,5,12,10,2,9,5,6,10,8,9,6],
    [9,5,5,13,13,5,5,12,9,5,5,12]
    ])

''' maze 01 map_wall form
(6, 12,  4,  6, 10, 10, 14, 14, 10,  8,  6, 12)
(5,  7, 13,  7, 10, 10, 13,  3, 14, 14,  9,  5)
(5,  5,  5,  5,  4,  6, 11, 14,  9,  7,  8,  5)
(7,  9,  3,  9,  7, 11, 14,  9,  6, 15, 10,  9)
(5,  4,  6, 12,  7, 10,  9,  6, 13,  5,  6, 12)
(7, 15, 13,  5,  5,  6, 14, 13,  7, 13,  5,  5)
(5,  5,  7, 13,  5,  3,  9,  3, 13,  7,  9,  5)
(5,  7,  9,  3, 15, 10, 12,  2, 15,  9,  2, 13)
(5,  3, 10, 12,  3, 14, 11, 12,  7, 10, 10, 13)
(7, 14, 10, 13,  6, 15, 12,  5,  1,  6, 12,  5)
(5,  5,  6,  9,  5,  5,  7, 13,  4,  5,  5,  5)
(1,  3, 11, 10,  9,  3,  9,  3, 11, 11, 11,  9)
'''

exp_maze_01 = np.array([
    [ 6, 12,  4,  6, 10, 10, 14, 14, 10,  8,  6, 12],
    [ 5,  7, 13,  7, 10, 10, 13,  9, 14, 14,  9,  5],
    [ 5,  5,  5,  5,  4,  6, 11, 14,  9,  7,  8,  5],
    [ 7,  9,  3,  9,  7, 11, 14,  9,  6, 15, 10,  9],
    [ 5,  4,  6, 12,  7, 10,  9,  6, 13,  5,  6, 12],
    [ 7, 15, 13,  5,  5,  6, 14, 13,  7, 13,  5,  5],
    [ 5,  0,  7, 13,  5,  3,  9,  3, 13,  7,  9,  5],
    [ 5,  7,  9,  9, 15, 10, 12,  2, 15,  9,  2, 13],
    [ 5,  9, 10, 12,  3, 14, 11, 12,  7, 10, 10, 13],
    [ 7, 14,  0, 13,  6, 15, 12,  5,  1,  6, 12,  5],
    [ 5,  5,  6,  9,  5,  5,  7, 13,  4,  5,  5,  5],
    [ 1,  3, 11, 10,  9,  3,  9,  3, 11, 11, 11,  9],
])

''' exp_maze text file form
(1, 5, 7, 5, 5, 5, 7, 5, 7, 5, 5, 6)
(3, 5, 14, 9, 7, 0, 15, 4, 9, 5, 7, 12)
(11, 6, 0, 10, 9, 7, 13, 6, 3, 5, 13, 4)
(10, 9, 13, 12, 9, 13, 5, 12, 9, 5, 7, 6)
(9, 5, 6, 3, 15, 5, 5, 7, 7, 4, 10, 10)
(3, 5, 15, 14, 10, 3, 6, 10, 11, 6, 10, 10)
(9, 7, 12, 11, 12, 9, 14, 9, 14, 11, 13, 14)
(3, 13, 5, 12, 2, 3, 13, 6, 9, 14, 9, 14)
(11, 4, 1, 7, 15, 13, 7, 13, 6, 9, 14, 10)
(11, 5, 6, 10, 9, 7, 13, 5, 15, 7, 14, 8)
(11, 5, 12, 10, 2, 9, 5, 6, 10, 8, 9, 6)
(9, 5, 5, 13, 13, 5, 5, 12, 9, 5, 5, 12)
'''

#transpose and rotate array to match final map
transp_1 = zip(*maze_01)
rot_1 = zip(*maze_01[::1])
fin_1 = rot_1[::-1]

for i in range(0,len(maze_01)):
    print fin_1[i]

print '\n'

transp_1 = zip(*exp_maze_01)
rot_1 = zip(*exp_maze_01[::-1])
#fin_1 = rot_1[::-1]

for i in range(0,len(maze_01)):
    print rot_1[i]
