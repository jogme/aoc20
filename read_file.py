def read_file(name):
    with open(name, "r") as f:
        lines = []
        for x in f:
            # removing trailing new line
            lines.append(x[:-1])
        return lines

def read_whole_file(name):
    with open(name, 'r') as f:
        return f.read()
