N = int(input())
A = list(map(int, input().split()))

ans = 0
len_A = len(A)
for i in range(len(A)):
    for j in range(i, len(A)):
        ans += (A[j] - A[i])**2

print(ans)
