dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    q = [[x, y]]
    d[x][y] = 1
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and d[nx][ny] == 0:
                    q.append([nx, ny])
                    d[nx][ny] = d[x][y] + 1


n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
d = [[0]*m for _ in range(n)]

bfs(0, 0)
print(d[n-1][m-1])