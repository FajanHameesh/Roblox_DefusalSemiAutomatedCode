def resistor(colors):
    colors = list(colors)
    lib = {
        'K':0,  # Black
        'b':1,  # Brown
        'R':2,
        'O':3,
        'Y':4,
        'G':5,  # Green
        'B':6,
        'P':7,
        'g':8,  # Gray
        'W':9,
    }

    result = (lib[colors[0]]*10 + lib[colors[1]]) * 10**(lib[colors[2]])
    return result

# while True:
#     inp = input('3 First Bands Color: ')
#     if inp == '':
#         break
#     print(f'\n{resistor(inp)}')