def mathematicss(text:str):
    text1 = text[0:2]
    text2 = text[2:4]

    lib = {
        'A':1,
        'B':3,
        'C':7,
        'D':2,
        'E':4,
        'F':5,
        'G':6,
        'H':0,
        'I':8,
        'J':9,
    }

    result = ( lib[text1[0]]*10 + lib[text1[1]] ) * (lib[text2[0]]*10 + lib[text2[1]]) 
    return result

# while True:
#     inp = input("Text: ")
#     if inp == '':
#         break

#     print(mathematicss(inp))