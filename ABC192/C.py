def f(x: int):
    sort_x = sorted(str(x), reverse=True)
    g1 = int(''.join(sort_x))
    sort_x.sort()
    g2 = int(''.join(sort_x))
    return g1 - g2


def A(N, K):
    a = N
    for _ in range(K):
        a = f(a)
    print(a)


N, K = tuple(map(int, input().split()))
A(N, K)
