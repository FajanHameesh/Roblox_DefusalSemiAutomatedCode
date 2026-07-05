def light(startCol,serial):
    serial = int(serial)
    lib = {
        'R':5,
        'Y':10,
        'B':7,
        'G':4,
        'W':6,
    }
    result = lib[startCol]*serial
    if result >= 80:
        final = "StartColor"
    elif result >= 70:
        final = 'Brown'
    elif result >= 60:
        final = 'Purple'
    elif result >= 50:
        final = 'Pink'
    elif result >= 40:
        final = 'White'
    elif result >= 30:
        final = 'Green'
    elif result >= 20:
        final = 'Yellow'
    elif result >= 10:
        final = 'Blue'
    elif result >= 0:
        final = 'Red'
    
    return final
