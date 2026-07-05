def tiles(code):
    lib = {
        'R':1,
        'G':9,
        'B':7,
        'Y':2,
        'P':6,
        'W':5,
    }

    result = lib[code[0]]+lib[code[1]]
    return result

# print(tiles(input("Enter Code: ")))