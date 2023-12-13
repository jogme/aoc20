import read_file
from copy import deepcopy

input = list(map(list, read_file.read_whole_file('eleven.input').split('\n')[:-1]))

def a():
    global input
    new_input = deepcopy(input)
    changed = True
    row_len = len(input)
    col_len = len(input[0])
    while changed:
        old_input = deepcopy(new_input)
        changed = False
        for x in range(row_len):
            for y in range(col_len):
                if old_input[x][y] == '.':
                    continue
                if old_input[x][y] == 'L' and \
                    (x-1 < 0 or y-1 < 0 or old_input[x-1][y-1] != '#') and \
                    (x-1 < 0 or old_input[x-1][y] != '#') and \
                    (x-1 < 0 or y+1 == col_len or old_input[x-1][y+1] != '#') and \
                    (y-1 < 0 or old_input[x][y-1] != '#') and \
                    (y+1 == col_len or old_input[x][y+1] != '#') and \
                    (x+1 == row_len or y-1 < 0 or old_input[x+1][y-1] != '#') and \
                    (x+1 == row_len or old_input[x+1][y] != '#') and \
                    (x+1 == row_len or y+1 == col_len or old_input[x+1][y+1] != '#'):
                        changed = True
                        new_input[x][y] = '#'
                elif old_input[x][y] == '#':
                    occupied = 0
                    if x-1 >= 0 and y-1 >= 0 and old_input[x-1][y-1] == '#':
                        occupied += 1
                    if x-1 >= 0 and old_input[x-1][y] == '#':
                        occupied += 1
                    if x-1 >= 0 and y+1 != col_len and old_input[x-1][y+1] == '#':
                        occupied += 1
                    if y-1 >= 0 and old_input[x][y-1] == '#':
                        occupied += 1
                    if y+1 != col_len and old_input[x][y+1] == '#':
                        occupied += 1
                    if x+1 != row_len and y-1 >= 0 and old_input[x+1][y-1] == '#':
                        occupied += 1
                    if x+1 != row_len and old_input[x+1][y] == '#':
                        occupied += 1
                    if x+1 != row_len and y+1 != col_len and old_input[x+1][y+1] == '#':
                        occupied += 1
                    if occupied > 3:
                        changed = True
                        new_input[x][y] = 'L'

    occupied = 0
    for y in new_input:
        occupied += y.count('#')
    return occupied

print(a())

# L => true
# eof => true
# # => false
def visibility(x, y, posX, posY, old_input):
    while True:
        posX += x
        posY += y

        if posX < 0 or posX == len(old_input) or posY < 0 or posY == len(old_input[0]) or old_input[posX][posY] == 'L':
            return True
        if old_input[posX][posY] == '#':
            return False

def b():
    global input
    new_input = deepcopy(input)
    changed = True
    row_len = len(input)
    col_len = len(input[0])
    while changed:
        old_input = deepcopy(new_input)
        changed = False
        for x in range(row_len):
            for y in range(col_len):
                if old_input[x][y] == '.':
                    continue
                if old_input[x][y] == 'L' and \
                    (x-1 < 0 or y-1 < 0 or visibility(-1,-1,x,y,old_input)) and \
                    (x-1 < 0 or visibility(-1,0,x,y,old_input)) and \
                    (x-1 < 0 or y+1 == col_len or visibility(-1,+1,x,y,old_input)) and \
                    (y-1 < 0 or visibility(0,-1,x,y,old_input)) and \
                    (y+1 == col_len or visibility(0,+1,x,y,old_input)) and \
                    (x+1 == row_len or y-1 < 0 or visibility(+1,-1,x,y,old_input)) and \
                    (x+1 == row_len or visibility(+1,0,x,y,old_input)) and \
                    (x+1 == row_len or y+1 == col_len or visibility(+1,+1,x,y,old_input)):
                        changed = True
                        new_input[x][y] = '#'
                elif old_input[x][y] == '#':
                    occupied = 0
                    if x-1 >= 0 and y-1 >= 0 and not visibility(-1,-1,x,y,old_input):
                        occupied += 1
                    if x-1 >= 0 and not visibility(-1,0,x,y,old_input):
                        occupied += 1
                    if x-1 >= 0 and y+1 != col_len and not visibility(-1,+1,x,y,old_input):
                        occupied += 1
                    if y-1 >= 0 and not visibility(0,-1,x,y,old_input):
                        occupied += 1
                    if y+1 != col_len and not visibility(0,+1,x,y,old_input):
                        occupied += 1
                    if x+1 != row_len and y-1 >= 0 and not visibility(+1,-1,x,y,old_input):
                        occupied += 1
                    if x+1 != row_len and not visibility(+1,0,x,y,old_input):
                        occupied += 1
                    if x+1 != row_len and y+1 != col_len and not visibility(+1,+1,x,y,old_input):
                        occupied += 1
                    if occupied > 4:
                        changed = True
                        new_input[x][y] = 'L'

    occupied = 0
    for y in new_input:
        occupied += y.count('#')
    return occupied

print(b())
