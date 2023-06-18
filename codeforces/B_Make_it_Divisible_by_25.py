test_cases = int(input())

def min_operations(str_num):

    s = set()

    for i in range(1, len(str_num) + 1):

        if str_num[-i] in ['0', '5'] and '0' in s: # 00, 50.
            return i - 2

        if str_num[-i] == ['2', '7'] and '5' in s: # 25, 75.
            return i - 2

        s.add(str_num[-1])

for _ in range(test_cases):
    str_num = input()
    print(min_operations(str_num)) 




