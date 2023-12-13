import read_file

input = read_file.read_file('five.input')

def bisection(a, b, string, low_char, up_char):
    for char in string:
        if char == low_char:
            b = (a + b) // 2
        if char == up_char:
            a = round((a + b) / 2)
    return a if string[-1] == low_char else b
    
def a():
    max_id = 0
    for string in input:
        row = bisection(0,127, string[:-3], 'F', 'B')
        col = bisection(0,7, string[-3:], 'L', 'R')
        id = row * 8 + col
        max_id = id if id > max_id else max_id
    return max_id

print(str(a()))

def b():
    ids = []
    for string in input:
        row = bisection(0,127, string[:-3], 'F', 'B')
        col = bisection(0,7, string[-3:], 'L', 'R')
        ids.append(row * 8 + col)
    ids.sort()
    for i in range(1, len(ids)-1):
        if ids[i-1]+1 != ids[i]:
            return ids[i-1]+1

print(str(b()))
