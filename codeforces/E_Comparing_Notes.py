a = input()
b = input()
ai, aj = 0, len(a)-1
bi, bj = 0, len(b)-1

while ai < aj and a[ai] != '-':
    ai += 1

while aj > ai and a[aj] != '-':
    aj -= 1


while ai < bj and b[bi] != '-':
    bi += 1

while bj > bi and b[bj] != '-':
    bj -= 1

ai = min(ai, bi)
aj = max(aj, bj)
if a[:ai] != b[:ai] or a[aj:] != b[aj:]:
    print('NO')

else:
    print('YES')

     