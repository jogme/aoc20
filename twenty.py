import read_file

input = {int(x.split('\n')[0].split(' ')[1][:-1]):x.split('\n')[1:-1] if x.split('\n')[-1] == '' else x.split('\n')[1:] for x in read_file.read_whole_file('twenty.input').split('\n\n')}
sides = dict()
right = []
left = []
top = []
bot = []
for key in input:
    #left side
    sides[key] = [''.join([x[0] for x in input[key]])]
    #right side
    sides[key].append(''.join([x[-1] for x in input[key]]))
    all_sides += sides[key]
    all_sides.append(input[key][0])
    all_sides.append(input[key][-1])

# n = normal
# f = flipped
# r = rotated
# rf
def a():
    tiles = []
    for key1 in sides:
        # L R T B
        neighbours = [[]] * 4
        for key2 in sides:
            if key1 == key2:
                continue
            #right side
            if sides[key1][1] == sides[key2][0]:
                neighbours[1] = [key2, 'n']
            elif sides[key1][1] == sides[key2][1]:
                neighbours[1] = [key2, 'f']
            elif sides[key1][1] == sides[key2][1][::-1]:
                neighbours[1] = [key2, 'r']
            elif sides[key1][1] == sides[key2][0][::-1]:
                neighbours[1] = [key2, 'rf']
            #left side
            if sides[key1][0] == sides[key2][1]:
                neighbours[0] = [key2, 'n']
            elif sides[key1][0] == sides[key2][0]:
                neighbours[0] = [key2, 'f']
            elif sides[key1][0] == sides[key2][0][::-1]:
                neighbours[0] = [key2, 'r']
            elif sides[key1][0] == sides[key2][1][::-1]:
                neighbours[0] = [key2, 'rf']
            #top side
            if input[key1][0] == input[key2][-1]:
                neighbours[3] = [key2, 'n']
            elif input[key1][0] == input[key2][0]:
                neighbours[3] = [key2, 'rf']
            elif input[key1][0] == input[key2][0][::-1]:
                neighbours[3] = [key2, 'r']
            elif input[key1][0] == input[key2][-1][::-1]:
                neighbours[3] = [key2, 'f']
            #bottom side
            if input[key1][-1] == input[key2][0]:
                neighbours[3] = [key2, 'n']
            elif input[key1][-1] == input[key2][-1]:
                neighbours[3] = [key2, 'rf']
            elif input[key1][-1] == input[key2][-1][::-1]:
                neighbours[3] = [key2, 'r']
            elif input[key1][-1] == input[key2][0][::-1]:
                neighbours[3] = [key2, 'f']
        if len([x for x in neighbours if len(x) > 0]) > 2:
            tiles.append(key1)
            print(key1, neighbours)
    print(tiles)

print(len(all_sides))
all_sides = set(all_sides)
tmp = []
print(len(all_sides))
for x in all_sides:
    if not x[::-1] in all_sides:
        tmp.append(x)
print(len(tmp))
lalala = []
for key in input:
    for x in tmp:
        if x in input[key]:
            lalala.append(key)
d = dict()
for l in lalala:
    d[l] = lalala.count(l)
print(d)
