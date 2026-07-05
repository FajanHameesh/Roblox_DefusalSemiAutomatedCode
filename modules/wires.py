def wires(colors:str):
    condition1 = False
    if len(colors) == 3:
        if 'W' in colors:
            result = 'Second'
        elif 'B' in colors:
            result = 'First'
        elif 'R' in colors:
            result = 'First and Second'
        else:
            result = 'Last'

    elif len(colors) == 4 or len(colors) == 5:
        if len([i for i in colors if i == 'K']) == 2:
            result = 'First and Last'
        elif colors[-1] == 'W':
            result = 'Second Last'
        elif 'G' in colors:
            result = 'Green'
        else:
            result = 'Third'

    elif len(colors) == 6:
        for i in list(colors):
            if list(colors).count(i) == 3:
                condition1 = True
                break
        if condition1:
            result = 'First and Second'
        elif colors[4] == 'B' or colors[4] == 'R':
            result = 'Third'
        elif colors[5] != 'W':
            result = 'Last'
        elif 'Y' in colors:
            result = 'Third and Fifth'
        else:
            result = 'Fourth'
    return result

while True:
    inp = input("Wire Colors: ")
    if inp == '':
        break
    print(wires(inp))