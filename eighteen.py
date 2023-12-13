import read_file

input = read_file.read_file('eighteen.input')
parsed = list()

for i in input:
    a = [')' if x == '' else x for letter in i.split() for x in letter.split(')')]
    parsed.append(['(' if x == '' else x for char in a for x in char.split('(')])

def a():
    sum = 0
    for line in parsed:
        stack = []
        for char in line:
            try:
                num1 = int(char)
                if len(stack) != 0 and (stack[-1] == '+' or stack[-1] == '*'):
                    op = stack.pop()
                    num = stack.pop()
                    if op == '+':
                        stack.append(num+num1)
                    else: # op == '*'
                        stack.append(num*num1)
                else:
                    stack.append(num1)
            except:
                if char == '+' or char == '*':
                    stack.append(char)
                elif char == '(':
                    stack.append(char)
                else: #char == ')':
                    num1 = stack.pop()
                    stack.pop() # '('
                    if len(stack) != 0:
                        if stack[-1] == '+':
                            stack.pop()
                            num = stack.pop()
                            stack.append(num+num1)
                        elif stack[-1] == '*':
                            stack.pop()
                            num = stack.pop()
                            stack.append(num*num1)
                        else:
                            stack.append(num1)
                    else:
                        stack.append(num1)
        sum += stack[0]
    return sum

print(a())

def b():
    sum = 0
    for line in parsed:
        stack = []
        for char in line:
            try:
                num1 = int(char)
                if len(stack) != 0:
                    if stack[-1] == '+':
                        op = stack.pop()
                        num = stack.pop()
                        stack.append(num+num1)
                    else:
                        stack.append(num1)
                else:
                    stack.append(num1)
            except:
                if char == '+' or char == '*':
                    stack.append(char)
                elif char == '(':
                    stack.append(char)
                else: #char == ')':
                    num1 = stack.pop()
                    char_stack = stack.pop() # '('
                    if char_stack == '(':
                        if len(stack) != 0:
                            if stack[-1] == '+':
                                stack.pop()
                                num = stack.pop()
                                stack.append(num+num1)
                            else:
                                stack.append(num1)
                        else:
                            stack.append(num1)
                    else: #char_stack == '*'
                        mul = num1
                        while char_stack != '(':
                            mul *= stack.pop()
                            char_stack = stack.pop()
                        if len(stack) != 0 and stack[-1] == '+':
                            stack.pop()
                            stack.append(stack.pop()+mul)
                        else:
                            stack.append(mul)
        if len(stack) > 1:
            mul = 1
            while len(stack) != 1:
                mul *= stack.pop()
                char_stack = stack.pop()
            stack.append(mul*stack.pop())
        sum += stack[0]
    return sum

print(b())
