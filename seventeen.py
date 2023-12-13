import read_file
import copy

input = read_file.read_file('seventeen.input')

def a():
    active = []
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    zmin = -1
    zmax = 1
    for i_r, row in enumerate(input):
        for i_c, char in enumerate(row):
            if char == '#':
                active.append([i_r,i_c,0])
                xmin = i_r-1 if i_r == xmin else xmin
                xmax = i_r+1 if i_r == xmax else xmax
                ymin = i_c-1 if i_c == ymin else ymin
                ymax = i_c+1 if i_c == ymax else ymax
    buffer_active = copy.deepcopy(active)

    for cycle in range(6):
        for z in range(zmin, zmax+1):
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    act_neigh = 0
                    for zd in range(-1,2):
                        for xd in range(-1,2):
                            for yd in range(-1,2):
                                if (xd != 0 or yd != 0 or zd != 0) and [x+xd,y+yd,z+zd] in active:
                                    act_neigh += 1
                    if [x,y,z] in active:
                        if act_neigh != 2 and act_neigh != 3:
                            buffer_active.remove([x,y,z])
                    else:
                        if act_neigh == 3:
                            buffer_active.append([x,y,z])
                            xmin = x-1 if x == xmin else xmin
                            xmax = x+1 if x == xmax else xmax
                            ymin = y-1 if y == ymin else ymin
                            ymax = y+1 if y == ymax else ymax
                            zmin = z-1 if z == zmin else zmin
                            zmax = z+1 if z == zmax else zmax
        active = copy.deepcopy(buffer_active)
    return len(buffer_active)

print(a())

def b():
    active = []
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    zmin = -1
    zmax = 1
    wmin = -1
    wmax = 1
    for i_r, row in enumerate(input):
        for i_c, char in enumerate(row):
            if char == '#':
                active.append([i_r,i_c,0,0])
                xmin = i_r-1 if i_r == xmin else xmin
                xmax = i_r+1 if i_r == xmax else xmax
                ymin = i_c-1 if i_c == ymin else ymin
                ymax = i_c+1 if i_c == ymax else ymax
    buffer_active = copy.deepcopy(active)

    for cycle in range(6):
        for z in range(zmin, zmax+1):
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    for w in range(wmin, wmax+1):
                        act_neigh = 0
                        for zd in range(-1,2):
                            for xd in range(-1,2):
                                for yd in range(-1,2):
                                    for wd in range(-1,2):
                                        if (xd != 0 or yd != 0 or zd != 0 or wd != 0) and [x+xd,y+yd,z+zd,w+wd] in active:
                                            act_neigh += 1
                        if [x,y,z,w] in active:
                            if act_neigh != 2 and act_neigh != 3:
                                buffer_active.remove([x,y,z,w])
                        else:
                            if act_neigh == 3:
                                buffer_active.append([x,y,z,w])
                                xmin = x-1 if x == xmin else xmin
                                xmax = x+1 if x == xmax else xmax
                                ymin = y-1 if y == ymin else ymin
                                ymax = y+1 if y == ymax else ymax
                                zmin = z-1 if z == zmin else zmin
                                zmax = z+1 if z == zmax else zmax
                                wmin = w-1 if w == wmin else wmin
                                wmax = w+1 if w == wmax else wmax
        active = copy.deepcopy(buffer_active)
    return len(buffer_active)

print(b())
