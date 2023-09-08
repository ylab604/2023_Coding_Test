r,c,k=map(int,input().split())
map = []
for _ in range(r):
    map.append(list(input()))

##T 위치 파악
t=[]
for i in range(r):
    for j in range(c):
        if map[i][j] == 'T':
            t.append((i,j))
cnt = 0
#x,y = 시작 위치
dx=[-1,0,1,0]
dy=[0,-1,0,1]
visited = [[0]*c for _ in range(r)]

def dfs(depth,x,y):
    global cnt
    if depth == k:
        if (x,y) == (0,c-1):
            cnt+=1
        else:
            pass
        return


    #check visited
    visited[x][y] =1

    for i in range(4):
        nx =x+dx[i]
        ny =y+dy[i]
        #범위 안벗어난다면, 방문한적 없다면
        if 0<= nx < r and 0<= ny <c and visited[nx][ny] ==0 and map[nx][ny]!='T':
            visited[nx][ny]=1
            dfs(depth+1,nx,ny)
            visited[nx][ny]=0


dfs(1,r-1,0)
print(cnt)
