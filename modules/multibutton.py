def multi(code):
    code = [int(i) for i in code]
    buttons_init = [
        ['R','Y','B'],
        ['O','G','P']
    ]
    session1 = []
    if code[1-1] < 6:
        session1.append(buttons_init[1-1][1-1])
        buttons_init[1-1][1-1] = '-'
    else:
        session1.append(buttons_init[2-1][1-1])
        buttons_init[2-1][1-1] = '-'

    if code[2-1] < 6:
        session1.append(buttons_init[1-1][2-1])
        buttons_init[1-1][2-1] = '-'
    else:
        session1.append(buttons_init[2-1][2-1])
        buttons_init[2-1][2-1] = '-'

    if code[3-1] < 6:
        session1.append(buttons_init[1-1][3-1])
        buttons_init[1-1][3-1] = '-'
    else:
        session1.append(buttons_init[2-1][3-1])
        buttons_init[2-1][3-1] = '-'
    session2 = []

    for i in buttons_init:
        for j in i:
            if j != '-':
                session2.append(j)

    if code[4-1] < 7:
        order = [2,3,1]
    elif code[5-1] < 7:
        order = [3,2,1]
    elif code[6-1] > 5:
        order = [1,2,3]
    else:
        order = [1,3,2]
    
    session2 = [session2[order[i]-1] for i in range(3)]
    result = "".join(session1) + "".join(session2)
    return result

# while True:
#     inp = input(f"\nCode: ")
#     if inp == '':
#         break
#     print(multi(inp))



