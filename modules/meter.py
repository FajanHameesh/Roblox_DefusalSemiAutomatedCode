def meter(psi):
    psi = int(psi)
    if psi > 10000:
        return 'Bright Green'
    elif psi > 8000:
        return 'Red'
    elif psi > 6000:
        return 'Orange'
    elif psi > 4000:
        return 'Yellow'
    elif psi > 2000:
        return 'Fade Green'
    elif psi > 0:
        return "Bright Green"
    elif psi < 0:
        return "Red"
    
# print(meter(input("Psi: ")))