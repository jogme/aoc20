import read_file

input = list(map(int, read_file.read_whole_file('fifteen.input').strip().split(',')))

#this solution is veeeeeeeeeery slow
def b(nth):
    for _ in range(len(input)+1, nth+1):
        if input[-1] in input[:-1]:
            i = input.index(input[-1])
            input[i] = -1
            input.append((len(input)-1 - i))
        else:
            input.append(0)
    return input[-1]

#time optimalized one
def c(nth):
    dd = dict()
    for i,x in enumerate(input):
        dd[x] = i+1
    dd.popitem()
    last = input[-1]
    for count in range(len(input)+1, nth+1):
        if last in dd:
            tmp = count-1-dd[last]
            dd[last] = count-1
            last = tmp
        else:
            dd[last] = count-1
            last = 0
    return last

print(c(2020))

print(c(30000000))
