#상하좌우
import copy
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
###cctv 방향
mode=[
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]],
]
cctv=[]
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] !=6:
            cctv.append([i,j,arr[i][j]])

def check(arr,mode,x,y):
    cnt_check=0
    for i in mode:
        nx=x
        ny=y

        while True:
            nx+= dx[i]
            ny+= dy[i]


            if nx<0 or ny <0 or nx>=n or ny>=m:
                break
            if arr[nx][ny]==6:
                break
            elif arr[nx][ny] ==0:
                arr[nx][ny] =-1


def dfs(depth,arr):
    global min_value
    if depth == len(cctv):
        cnt=0
        for i in range(n):
            cnt+=arr[i].count(0)
        min_value = min(min_value,cnt)
        return
    tmp = copy.deepcopy(arr)
    x,y,cctv_num = cctv[depth]
    for i in mode[cctv_num]:
        check(tmp,i,x,y)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)
시
min_value = int(1e9)
dfs(0,arr)
print(min_value)




