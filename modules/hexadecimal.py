def hexa(code):
    lib = {}
    code = [code[i:i+2] for i in range(0,len(code),2)]
    keys = '6162636465666768696A6B6C6D6E6F707172737475767778797A'
    keys = [[keys[i:i+2]] for i in range(0,len(keys),2)]
    values = 'abcdefghijklmnopqrstuvwxyz'
    values = list(values)
    for idx, j in enumerate(values):
        lib["".join(keys[idx])] = j
    
    result = [lib[i] for i in code]
    result = "".join(result)
    return result

# while True:
#     inp = input("Code: ")
#     if inp == '':
#         break
#     print(hexa(inp))
    

    