if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        com = input().split()
        if com[0]=='print':
            print(l)
        elif len(com)==3:
            l.insert(int(com[1]), int(com[2]))
        elif com[0] == 'remove':
            l.remove(int(com[1]))
        elif com[0] == 'append':
            l.append(int(com[1]))
        elif com[0] == 'sort':
            l.sort()
        elif com[0]=='pop':
            l.pop()
        elif com[0] =='reverse':
            l.reverse()
    