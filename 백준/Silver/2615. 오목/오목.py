bw = [list(map(int, input().split())) for _ in range(19)]
d = [[1, 0, 1, -1], [0, 1, 1, 1]]

def dfs(i, j):
    for k in range(4):
        ni, nj = i - d[0][k], j - d[1][k]
        if -1 < ni < 19 and -1 < nj < 19 and bw[i][j] == bw[ni][nj]:
            continue
        cnt = 1
        ni, nj = i + d[0][k], j + d[1][k]
        while -1 < ni < 19 and -1 < nj < 19 and bw[i][j] == bw[ni][nj]:
            cnt += 1
            ni, nj = ni + d[0][k], nj + d[1][k]
        if cnt == 5:
            print(bw[i][j])
            print(i + 1, j + 1)
            return True
    return False
    
for i in range(19):
    for j in range(19):
        if bw[i][j] == 0:
            continue
        if dfs(i, j):
            exit()
print(0)