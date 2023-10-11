mod = 179
mod2 = 197

a = input()
b = input()
positions = []

hash_b, hash_b2 = 0, 0
for i in range(len(b)):
    hash_b += ((ord(b[i])-96) * pow(27, i, mod)) %mod
    hash_b2 += ((ord(b[i])-96) * pow(27, i, mod)) %mod2
    hash_b %= mod
    hash_b2 %= mod2

hash_a, hash_a2 = 0, 0
for i in range(1, len(a)):
    hash_a += ((ord(a[i])-96) * pow(27, i-1, mod)) %mod
    hash_a2 += ((ord(a[i])-96) * pow(27, i-1, mod)) %mod2
    hash_a %= mod
    hash_a2 %= mod2

if hash_a == hash_b and hash_a2==hash_b2:
    positions.append(1)

for i in range(1, len(a)):
    hash_a += ((ord(a[i-1]) - ord(a[i]) )* (pow(27, i-1, mod))) %mod
    hash_a2 += ((ord(a[i-1]) - ord(a[i]) )* (pow(27, i-1, mod))) %mod2

    hash_a %= mod
    hash_a2 %= mod2

    if hash_a == hash_b and hash_a2 == hash_b2:
        positions.append(i+1)
# diff_substrings.add(hash_val)
# for i in range(2, n):
#     hash_val += (ord(s[i-2]) - ord(s[i]) )* (pow(27, i-2, mod))
#     diff_substrings.add(hash_val)
# print(len(diff_substrings))
print(len(positions))
print(*positions)