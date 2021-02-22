def three_point_shot(x, y):
    if x > y:
        if x < y + 3:
            print('Yes')
        else:
            print('No')
    elif x < y:
        if x + 3 > y:
            print('Yes')
        else:
            print('No')


x, y = map(int, input().split())
three_point_shot(x, y)
