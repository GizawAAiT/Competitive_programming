import textwrap

def wrap(string, w):
    res = ''
    while len(string)> w:
        res += string[:w]
        res += '\n'
        string = string[w:]
    res += string
    return res
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)