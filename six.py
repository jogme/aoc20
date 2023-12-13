import read_file

input = read_file.read_whole_file('six.input')

def a():
    count = 0
    groups = input.split('\n\n')
    for g in groups:
        persons = g.split('\n')
        g_ans = set()
        for p in persons:
            g_ans |= set(p)
        count += len(g_ans)
    return count

print(str(a()))

def b():
    count = 0
    groups = input.split('\n\n')
    for g in groups:
        persons = g.split('\n')
        g_ans = True
        for p in persons:
            if g_ans == True:
                g_ans = set(p)
            g_ans &= set(p)
        count += len(g_ans)
    return count

print(str(b()))
