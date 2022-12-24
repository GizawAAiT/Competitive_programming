# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K, elements = int(input()), list(map(int, input().split()))
for element, count in Counter(sorted(elements)).items():
    if count == 1:
        print(element)
        break