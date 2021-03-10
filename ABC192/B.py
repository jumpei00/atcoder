S = input()
odd = ''
even = ''
for i, s in enumerate(S):
    if (i + 1) % 2 == 0:
        even += s
    else:
        odd += s

if odd.islower() and not even:
    print('Yes')
elif odd.islower() and even.isupper():
    print('Yes')
else:
    print('No')
