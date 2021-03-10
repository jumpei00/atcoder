def abc_tournament(n, a):
    N = 2 ** n
    pre_a = a[:int(N / 2)]
    forward_a = a[int(N / 2):]

    pre_a_max = max(pre_a)
    forward_a_max = max(forward_a)
    if pre_a_max < forward_a_max:
        r = a.index(pre_a_max) + 1
    elif pre_a_max > forward_a_max:
        r = a.index(forward_a_max) + 1

    print(r)


n = int(input())
a = list(map(int, input().split()))
abc_tournament(n, a)
