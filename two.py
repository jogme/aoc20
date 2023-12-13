def read_file(name):
    f = open(name, "r")
    lines = []
    for x in f:
        # removing trailing new line
        lines.append(x[:-1])
    return lines

input = read_file('two.input')

def a(data):
    counter = 0
    for x in data:
        policy, pswd = x.split(': ')
        minC, maxC = policy.split('-')
        maxC, char = maxC.split(' ')
        tmp = pswd.count(char)
        if tmp >= int(minC) and tmp <= int(maxC):
            counter += 1
    return counter

print('a: '+str(a(input)))

def b(data):
    counter = 0
    for x in data:
        policy, pswd = x.split(': ')
        posX, posY = policy.split('-')
        posY, char = posY.split(' ')
        if (pswd[int(posX)-1] == char) != (pswd[int(posY)-1] == char):
            counter += 1
    return counter

print('b: '+str(b(input)))
