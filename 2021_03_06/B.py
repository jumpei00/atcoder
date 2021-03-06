N = int(input())
A = []
B = []
for _ in range(N):
    a, b = tuple(map(int, input().split()))
    A.append(a)
    B.append(b)

ans = 10 ** 5 + 10 ** 5
for ai, a in enumerate(A):
    for bi, b in enumerate(B):
        if ai == bi:
            ans = min(ans, a + b)
        else:
            ans = min(ans, max(a, b))

print(ans)
