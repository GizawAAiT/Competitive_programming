t = int(input())
for _ in range(t):
    chess = []
    input()
    for i in range(8):
        chess.append(''.join(input().split()))
    # print(chess)
    for i in range(1,7):
        for j in range(1,7):
            if chess[i-1][j-1] =='#' and  chess[i+1][j+1] =='#' and  chess[i+1][j-1] =='#' and  chess[i-1][j+1] == '#':
                print(i+1,j+1)
                break
