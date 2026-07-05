def button(text,color):
    click_count = 0

    if text == 'nothing':
        click_count += 1
    elif color == 'R':
        click_count += 2
    elif text == '':
        click_count += 3
    elif color == 'W':
        click_count += 4
    elif text == 'notext':
        click_count += 5
    elif color == 'G':
        click_count += 6
    else:
        click_count = 0
    
    if click_count <= 3:
        arrow = 'down'
    else:
        arrow = 'up'
    
    return (f'\nClick {click_count} times and click {arrow} arrow.\n')
