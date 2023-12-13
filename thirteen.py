import read_file

input = read_file.read_file('thirteen.input')

t = int(input[0])
buses = list(map(int,filter(lambda a: a != 'x', input[1].split(','))))

def a():
    tmp = [x-(t % x) for x in buses]
    return buses[tmp.index(min(tmp))] * min(tmp)

print(a())

def b():
    offset = input[1].split(',')
    offset = [offset.index(str(x)) for x in buses]
    biggest = max(buses)
    big_i = buses.index(biggest)
    i = 100000000000000
    i += biggest-(i % biggest)
    while True:
        for x in range(len(buses)):
            if x == big_i:
                continue
            if x < big_i:
                if (i - offset[x]) % buses[x] != 0:
                    break
            else:
                if (i + offset[x]) % buses[x] != 0:
                    break
        i += biggest
    return i

def bb():
    offset = input[1].split(',')
    for x in buses:

    
print(b())
