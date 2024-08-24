


def r_search(maze, row, col):
   
    x = col + 1

    if maze[row][x] == 'p':
        return True , maze, row, x

    else:
        return False, maze, row, col

def search(maze, n,  row, col):

    for i in range(0, n):
        if (maze[i][col]) == 'p':
            maze[i][col] = '*'
            return maze, i, col

def u_search(maze, row, col):
    x = row - 1
    if maze[x][col] == 'p':
        return True, maze, x, col

    else:
        return False, maze, row, col

def d_search(maze, row, col):
    x = row + 1
    if maze[x][col] == 'p':
        return True, maze, x, col

    else:
        return False, maze, row, col

def l_search(maze, row, col):
    x = col - 1
    if maze[row][x] == 'p':
        return True, maze, row, x

    else:
        return False, maze, row, col

####### MAIN PART OF CODE #####
n = int(input('Enter the amount of rows in the maze: '))

maze = []
maze2 = maze.copy()

for i in range(0, n):
    print('Enter row', i+1, 'of the Labyrinth:')
    r = input()

    r = list(r)
    maze.append(r)

maze, new_r, new_c = search(maze, n, 0 , 0)

Tmoves = [[new_r, new_c]]
moves = [[new_r, new_c]]

while new_c != len(maze[0])-1:

    a, b, c, d = u_search(maze, new_r, new_c)
    w, x, y, z = d_search(maze, new_r, new_c)
    m, o, p, q = r_search(maze, new_r, new_c)
    h, i, j, k = l_search(maze, new_r, new_c)
    
    if a == True and w == False and m == False and h == False:
        new_r = c
        new_c = d
        moves.append([new_r, new_c])
        maze[c][d] = '*'
        
    elif w == True and a == False and m == False and h == False:
        new_r = y
        new_c = z
        moves.append([new_r, new_c])
        maze[y][z] = '*'

    elif m == True and a == False and w == False and h == False:
        new_r = p
        new_c = q
        moves.append([new_r, new_c])
        maze[p][q] = '*'

    elif h == True and a == False and w == False and m == False:
        new_r = j
        new_c = k
        moves.append([new_r, new_c])
        maze[j][k] = '*'


    elif a == False and w == False and m == False and h == False:

        maze[new_r][new_c] = 'X'
        
        for j in moves:
            maze[j[0]][j[1]] = 'p'
            moves.remove(j)
            

        new_r = Tmoves[0][0]
        new_c = Tmoves[0][1]

    
    else:

        if m == True:
            new_r = p
            new_c = q
            moves.append([p, q])
            maze[p][q] = '*'

            
        elif a == True:
            new_r = c
            new_c = d
            moves.append([c, d])
            maze[c][d] = '*'


        elif w == True:
            new_r = y
            new_c = z
            moves.append([y, z])
            maze[y][z] = '*'

        elif h == True:
            new_r = j
            new_c = k
            moves.append([j, k])
            maze[j][k] = '*'
            
for i in moves:
    if moves.index(i)<moves.index([Tmoves[0][0], Tmoves[0][1]+1]):
        maze[i[0]][i[1]] = 'p'

maze[Tmoves[0][0]][Tmoves[0][1]] = '*'

print(' ')

for i in range(0, n):
    for j in range(0, len(maze[0])):
        print(maze[i][j], end = '')

    print(' ')



