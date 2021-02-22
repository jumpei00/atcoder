X = input()
M = int(input())

max_num = int(max(list(X))) + 1

ans = 0
while True:
    out = 0
    for i in range(1, len(X) + 1):
        out += int(X[-i]) * (max_num ** (i - 1))
    if out > M:
        break
    max_num += 1
    ans += 1

print(ans)
