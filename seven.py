import read_file
import re

input = read_file.read_file('seven.input')

d_a = {}
d_b = {}

def a_r(key):
    global d_a
    l = set()
    for e in d_a:
        if key in d_a[e]:
            l.add(e)
            l |= a_r(e)
    return l

def a():
    global d_a
    for line in input:
        if 'no other' in line:
            continue
        arr = line.split(' bags contain ')
        key = arr[0]
        values = re.sub('\d', '', arr[1][:-1]).replace(' bags', '').replace(' bag', '').lstrip().split(',  ')
        d_a[key] = values
    return len(a_r("shiny gold"))

print(a())

def b_r(value):
    global d_b
    count = 0
    if value == '':
        return 0
    for e in value:
        color = e.split(' ', 1)
        count += int(color[0]) + int(color[0]) * b_r(d_b[color[1]])
    return count

def b():
    global d_b
    for line in input:
        arr = line.split(' bags contain ')
        key = arr[0]
        if 'no other' in line:
            d_b[key] = ''
            continue
        values = arr[1][:-1].replace(' bags', '').replace(' bag', '').lstrip().split(', ')
        d_b[key] = values
    return b_r(d_b['shiny gold'])

print(b())
