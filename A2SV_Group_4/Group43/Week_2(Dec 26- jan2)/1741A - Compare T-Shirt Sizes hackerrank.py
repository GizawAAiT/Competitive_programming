t = int(input())

size = {'M':2, "S":1, 'L':3}

for _ in range(t):
    a, b = input().split()
    if size[a[-1]]==size[b[-1]]:
        if len(a)==len(b): print('=')
        elif a[-1]=='L' and len(a)>len(b) or a[-1]=='S' and len(a)<len(b): 
            print('>')
        else: print('<')
    elif size[a[-1]]>size[b[-1]]: print('>')
    else: print('<')
    