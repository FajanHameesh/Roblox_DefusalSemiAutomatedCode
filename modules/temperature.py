def temp(code):
    shapes = code[0:3]
    colors = code[3:5]

    shapeLib = {
        'S':-1,
        'C':1,
        'T':0
    }
    colorLib = {
        'B':1,
        'Y':2,
        'R':3,
        'K':4,
    }

    X = sum( [shapeLib[i] for i in shapes] )
    Y = colorLib[colors[0]] * colorLib[colors[1]]
    Z = X*Y
    result = 100 + Z
    return result

# while True:
#     inp = input("\nCode (ShapeColors): ")
#     if inp == '':
#         break
#     print(f"Set Temp to {temp(inp)}")
