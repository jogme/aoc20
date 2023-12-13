import read_file

input = read_file.read_file('three.input')

def a():
    column = 0
    trees = 0

    for x in input:
        if x[column % 31] == '#':
            trees += 1
        column += 3
    return trees

print(str(a()))

def b(row_delta, column_delta):
    column = 0
    trees = 0

    for n, x in enumerate(input):
        if n % row_delta:
            continue
        if x[column % 31] == '#':
            trees += 1
        column += column_delta
    return trees

print(str(b(1,1)*b(1,3)*b(1,5)*b(1,7)*b(2,1)))
