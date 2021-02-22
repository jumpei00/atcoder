def orthogonality(n, a, b):
    r = 0
    for a_i, b_i in zip(a, b):
        r += a_i * b_i

    if r == 0:
        print('Yes')
    else:
        print('No')


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
orthogonality(n, a, b)
