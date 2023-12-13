import read_file
import copy

input = read_file.read_whole_file('sixteen.input').rstrip().split('\n\n')
rules = {line.split(': ')[0]:[a for x in line.split(': ')[1].split(' or ') for a in list(map(int,x.split('-')))] for line in input[0].split('\n')}
my_ticket = list(map(int, input[1].split(':\n')[1].split(',')))
nearby_tickets = [list(map(int, x.split(','))) for x in input[2].split(':\n')[1].split('\n')][:-1]
valid_nearby_tickets = copy.deepcopy(nearby_tickets)

def a():
    sum = 0
    for n_ticket in nearby_tickets:
        for val in n_ticket:
            valid = False
            for c_val in rules.values():
                if (c_val[0] <= val and c_val[1] >= val) or (c_val[2] <= val and c_val[3] >= val):
                    valid = True
                    break
            if not valid:
                sum += val
                #line for part b
                if n_ticket in valid_nearby_tickets:
                    valid_nearby_tickets.remove(n_ticket)
                #end line for part b
    return sum

print(a())

# This function is not working perfectly.
# with my input 'arrival_platform' and 'row' has the same 2
# values at the end which this algorithm doesn't await
# and 'type' should be 3 (containing the two values of row
# and arrival_platform)
# for the solution I don't need those values
# so I decided to ignore it
def b():
    key_pos = {x:set() for x in rules.keys()}
    for n_ticket in valid_nearby_tickets:
        for index, val in enumerate(n_ticket):
            for key in rules:
                c_val = rules[key]
                if (c_val[0] > val or c_val[1] < val) and (c_val[2] > val or c_val[3] < val):
                    key_pos[key].add(index)
        for index, val in enumerate(my_ticket):
            for key in rules:
                c_val = rules[key]
                if (c_val[0] > val or c_val[1] < val) and (c_val[2] > val or c_val[3] < val):
                    key_pos[key].add(index)
    for key in key_pos:
        key_pos[key] = list({0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19} - key_pos[key])
    sorted_keys = sorted(key_pos, key=lambda key: len(key_pos[key]))
    for key in sorted_keys:
        if len(key_pos[key]) == 1:
            for key_del in key_pos:
                if key == key_del:
                    continue
                if key_pos[key][0] in key_pos[key_del]:
                    key_pos[key_del].remove(key_pos[key][0])
    sum = 1
    for key in key_pos:
        if 'departure' in key:
            sum *= my_ticket[key_pos[key][0]]
    return sum

print(b())
