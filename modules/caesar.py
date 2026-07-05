def caesar(code,serial):
    serial = [int(i) for i in serial]
    shift = sum(serial)
    if shift % 25 == 0:
        shift = shift // 25
    alfabet = list('abcdefghijklmnopqrstuvwxyz')
    code_idx = [alfabet.index(i) for i in code]
    new_idx = [i-shift for i in code_idx]
    new_code = [alfabet[i] for i in new_idx]
    result = "".join(new_code)
    return result

# while True:
#     inp1 = input(f"\nCode: ")
#     inp2 = input("Serial Numbers: ")
#     if inp1 == '':
#         break
#     print(caesar(inp1,inp2))


