import read_file
import re

input = read_file.read_whole_file('nineteen.input').split('\n\n')
rules = input[0].split('\n')
msgs = input[1].split('\n')[:-1]

rules = {r.split(': ')[0]:r.split(': ')[1].split() for r in rules}
options = []
options.append(rules['0'])
made_options = []

def a():
    index = 0
    while True:
        if len(options) == 0:
            break
        while True:
            if len(options[0]) == 0:
                break
            rule_no = rules[options[0].pop(0)]
            if '"a"' in rule_no or '"b"' in rule_no:
                try:
                    made_options[index] += rule_no[0].replace('"','')
                except:
                    made_options.append(rule_no[0].replace('"',''))
                continue
            elif '|' in rule_no:
                options.append(rule_no[rule_no.index('|')+1:] + options[0])
                options[0] = rule_no[:rule_no.index('|')] + options[0]
            else:
                options[0] = rule_no + options[0]
        options.pop(0)
        index += 1

def rec_expand(item):
    if len(item) == 1 and (item[0] == 'a' or item[0] == '"a"'):
        return 'a'
    elif len(item) == 1 and (item[0] == 'b' or item[0] == '"b"'):
        return 'b'
    elif re.fullmatch(r'[ab()|]*', ''.join(item)):
        return item
    tmp = []
    for element in item:
        if element != '|' and element != '(' and element != ')' and element != '+' and element != '[' and element != ']':
            # changes for b
            if element == '8':
                rules[element] = ['(', '42', ')', '+']
            if element == '11':
                rules[element] = ['(', '42', '31', '|', '42', '42', '31', '31', '|', '42', '42', '42', '31', '31', '31', '|', '42', '42', '42', '42', '31', '31', '31', '31', '|', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '|', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '|', '42', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', ')']
            # end changes for b
            t = rec_expand(rules[element])
            if re.fullmatch(r'[ab()|]*', ''.join(t)):
                rules[element] = t
            tmp += t
        else:
            tmp.append(element)
    if '|' in tmp:
        return ['('] + tmp + [')']
    return tmp

##########################
# a)                     #
#   8: 42                #
#   11: 42 31            #
##########################
# b)                     #
#   8: 42 | 42 8         #
#   11: 42 31 | 42 11 31 #
##########################
def a_regex():
    for key in rules:
        rules[key] = ''.join(rec_expand(rules[key]))
    counter = 0
    for m in msgs:
        if re.fullmatch(rules['0'], m):
            counter += 1
    return counter

print(a_regex())
