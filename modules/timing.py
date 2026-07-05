def timing(code):
    num = code[0:2]
    letters = code[2:4]

    lib = {
        'A':2,
        'B':3,
        'C':7,
        'D':6,
        'E':4,
    }

    X = int(num[0]) + int(num[1])
    Y = lib[letters[0]] + lib[letters[1]]
    Z = X*Y

    if Z >= 100:
        result = 'Blue'
    elif Z >= 60:
        result = 'Green'
    elif Z >= 50:
        result = "Yellow"
    elif Z >= 40:
        result = "Blue"
    elif Z >= 30:
        result = "Red"
    elif Z >= 20:
        result = "Yello"
    elif Z >= 10:
        result = "Red"
    elif Z >= 0:
        result = 'Blue'
    return result

# while True:
#     inp = input("Code: ")
#     if inp == '':
#         break
#     print(f'Click when the display is {timing(inp)}')