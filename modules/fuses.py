def fuses(code1,code2):
    color_lib = {
        'R': 1,
        'Y': 2,
        'G': 3,
        'B': 4,
    }
    colors = list(code1)
    wired = code2
    result = []
    for idx,i in enumerate(colors):
        if str(idx+1) not in wired:
            result.append(0)
        else:
            result.append(color_lib[i])
    
    return "".join([str(i) for i in result])
    