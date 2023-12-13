import read_file
import math

input = list(map(int, read_file.read_file("ten.input")))
input.sort()
input.insert(0, 0)
input.append(input[-1]+3)

def a():
    arr = [y-x for x,y in zip(input, input[1:])]
    return arr.count(1)*arr.count(3)

print(a())

def b():
    arr = [y-x for x,y in zip(input, input[1:])]
    count = 0
    for x in range(len(arr)-1):
        if arr[x] + arr[x+1] == 2:
            count += 1
            try:
                if arr[x+2] == 1:
                    count += 1
            except:
                continue
    total = 0
    for f in range(1, count):
        total += math.factorial(count)//(math.factorial(f)*math.factorial(count-f))

    return total

print(b())
