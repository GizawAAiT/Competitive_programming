s = input()
first_ab, last_ab, first_ba, last_ba = [float('inf'), -1, float('inf'), -1]
for i in range(len(s)-1):
    if s[i:i+2] == "AB":
        first_ab = i if first_ab == float("inf") else first_ab
        last_ab = i
    elif s[i:i+2] == "BA":
        first_ba = i if first_ba == float('inf') else first_ba
        last_ba = i

if first_ab != float('inf') and first_ba != float('inf') and (first_ab + 1 < last_ba or first_ba + 1 < last_ab):
    print("YES")

else:
    print("NO")
