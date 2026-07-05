def sliders(code,serial):
    lib = {
        'R':2,
        'Y':2,
        'B':3,
        'G':3,
        'P':4,
        'W':5,
        'g':5,
    }
    code = [lib[i] for i in code]
    serial = [int(i) for i in serial]

    if 4 in code:
        code[2] +=1
    if 2 in code:
        code[3] += 1
    if 3 in code:
        code[1] -= 1
    
    for i in serial:
        cond = i > 5
        if cond:
            code[1],code[3] = code[3],code[1]
            break
    
    for i in serial:
        cond = i < 5
        if cond:
            code[0],code[1] = code[1],code[0]
            break

    if 5 in serial:
        code[2],code[3] = code[3],code[2]
    result = "".join([str(i) for i in code])
    return result


# while True:
#     inp1 = input("Colors: ")
#     inp2 = input("Serial: ")
#     if inp1 == '':
#         break
#     print(sliders(inp1,inp2))
