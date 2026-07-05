def colorcode(colors,text):
    colLib = {
        'R':0,
        'G':0,
        'B':1,
        'Y':2,
        'W':3,
    }
    textLib = {
        'R':1,
        'G':3,
        'B':2,
        'Y':3,
        'W':4,
    }

    X = sum([textLib[i] for i in text])
    Y = sum([colLib[i] for i in colors])
    res = X-Y

    if res < 0:
        result = 0
    else:
        result = res
    return result

# while True:
#     inp1 = input(f"\nColors: ")
#     inp2 = input(f"Text: ")
#     if inp1 == '':
#         break
#     print(f"Click {colorcode(inp1,inp2)} times.")