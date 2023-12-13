import read_file

input = read_file.read_file('twelve.input')

def a():
    # N = 0
    # E = 90
    # S = 180
    # W = 270
    heading = 90
    # E/W,N/S
    pos = [0,0]
    for instr in input:
        i = instr[0]
        val = int(instr[1:])
        if i == 'F':
            if heading == 0:
                i = 'N'
            elif heading == 90:
                i = 'E'
            elif heading == 180:
                i = 'S'
            elif heading == 270:
                i = 'W'
        if i == 'N':
            pos[1] += val
        elif i == 'S':
            pos[1] -= val
        elif i == 'E':
            pos[0] += val
        elif i == 'W':
            pos[0] -= val
        elif i == 'R':
            heading += val
            heading %= 360
        elif i == 'L':
            heading -= val
            heading %= 360

    return abs(pos[0]) + abs(pos[1])

print(a())

def b():
    # [0] E/W | N/S [1]
    ship_pos = [0,0]
    waypoint = [10,1]
    for instr in input:
        i = instr[0]
        val = int(instr[1:])
        if i == 'F':
            ship_pos[0] += val*waypoint[0]
            ship_pos[1] += val*waypoint[1]
        elif i == 'N':
            waypoint[1] += val
        elif i == 'S':
            waypoint[1] -= val
        elif i == 'E':
            waypoint[0] += val
        elif i == 'W':
            waypoint[0] -= val
        elif i == 'R':
            for _ in range(val//90):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif i == 'L':
            for _ in range(val//90):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]

    return abs(ship_pos[0]) + abs(ship_pos[1])

print(b())
