def swap_case(s):
    res = []
    for char in s:
        res.append(char.lower()) if char.isupper() else res.append(char.upper())
    return ''.join(res)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)