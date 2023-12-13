import read_file

input = read_file.read_file('eight.input')

def a():
    acc = 0
    i = 0
    indexes = set()
    while True:
        if i in indexes:
            return acc
        indexes.add(i)
        instr, val = input[i].split()
        if instr == 'acc':
            acc += int(val)
        if instr == 'jmp':
            i += int(val)
            continue
        i += 1

print(a())

def b():
    notDone = True
    negJumps = set()
    iteration = 0
    while notDone:
        acc = 0
        i = 0
        indexes = set()
        changed = False
        while True:
            if i in indexes:
                break
            if len(input) == i:
                notDone = False
                break
            indexes.add(i)
            instr, val = input[i].split()
            if instr == 'acc':
                acc += int(val)
            if instr == 'jmp':
                if not changed and int(val) < 0 and i not in negJumps:
                    changed = True
                    negJumps.add(i)
                    i += 1
                    continue #making nop
                i += int(val)
                continue
            i += 1
        iteration += 1
    return acc

print(b())
