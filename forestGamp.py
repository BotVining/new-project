def gigati(x,y):
    if x > y:
        print('x = ', x)
    else:
        print('y = ', y)
    while True:
        x += 1
        if x > y:
            break
        else:
            y -= 1
        print('x - y = ', x - y)