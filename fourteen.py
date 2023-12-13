import read_file

input = list(map(lambda a: ''.join(a.split()).split('='), read_file.read_file('fourteen.input')))

def a():
    memory = dict()
    mask0 = ''
    mask1 = ''
    for x in input:
        if x[0] == 'mask':
            mask0 = int(x[1].replace('X', '1'), 2)
            mask1 = int(x[1].replace('X', '0'), 2)
        else:
            memory[x[0].split('[')[1][:-1]] = (int(x[1]) | mask1) & mask0
    return sum(memory.values())

print(a())

def b():
    memory = dict()
    mask = ''
    mask1 = ''
    for x in input:
        if x[0] == 'mask':
            mask = x[1]
            mask1 = int(x[1].replace('X', '0'), 2)
        else:
            addrs = [list('{0:b}'.format(int(x[0].split('[')[1][:-1]) | mask1).zfill(36))]
            for i,maskx in enumerate(mask):
                if maskx == 'X':
                    addrs[0][i] = 'X'
            addrs[0] = ''.join(addrs[0])
            for count in range(mask.count('X')):
                tmp = list()
                for i,y in enumerate(addrs):
                    tmp.append(y.replace('X', '0', 1))
                    tmp.append(y.replace('X', '1', 1))
                addrs = tmp
            for addrx in addrs:
                memory[addrx] = int(x[1])
    return sum(memory.values())

print(b())
