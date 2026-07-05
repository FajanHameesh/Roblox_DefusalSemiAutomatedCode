def binary(code):

    if '1' not in code:
        return 1
    elif code[2-1] == '1' and code[7-1] == '0':
        return 2
    elif code[1-1] == '1' and code[2-1] == '1':
        return 3
    elif code[1-1] == '0' and code[7-1] == '0':
        return 4
    elif code[1-1] == '1' and code[3-1] == '1':
        return 5
    elif sum([int(i) for i in code]) > 3:
        return 6
    elif sum([int(i) for i in code]) < 3:
        return 7
    else:
        return 0

# while True:
#     inp = input("Kondisi Lampu: ")
#     if inp == '':
#         break

#     print(f'Klik {binary(inp)} kali.')