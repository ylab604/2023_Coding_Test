##조합 구현
n,m = map(int,input().split())
#0은 빈칸 1은 벽 2는 비활성 바이러스 위치
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
check=[]
wall=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            check.append([i,j,0])
        if arr[i][j]==1:
            wall.append([i,j])

combi=[]
tmp=[]
"""def dfs(tmp,depth):
    global combi
    if depth ==m:
        #중복 체크
        a = sorted(tmp)
        if a not in combi:
            combi.append(a[:])
            #print(a)
            #print(combi)
        return
    for i in check:
        if i not in tmp:
            tmp.append(i)
            dfs(tmp,depth+1)
            tmp.pop()
dfs(tmp,0)"""
from itertools import combinations
for c in list(combinations(check, m)):
    combi.append(c)

result=1e9
#print(len(combi))
#좌상우하
dx = [0,-1,0,1]
dy = [-1,0,1,0]
from collections import deque
from copy import deepcopy
for k in combi:

    q = deque()
    visited = [[0] * n for _ in range(n)]
    new_arr = deepcopy(arr)
    #for aa in wall:
    #    visited[aa[0]][aa[1]]=1


    for virus in k:
        q.append(virus)
        visited[virus[0]][virus[1]] = 1
        new_arr[virus[0]][virus[1]] = -2

    last_cnt=0
    while q:
        n_x,n_y,cnt = q.popleft()
        #입력 제거하고 업뎃되는 모든 값을 q에 받아야함
        for i in range(4):
            nx = n_x + dx[i]
            ny = n_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                # 벽을 만나면 스킵
            if new_arr[nx][ny] == 1:
                continue
                # 빈칸 & 활성화
            if not new_arr[nx][ny] == 1 and not visited[nx][ny]==1:
                visited[nx][ny] = 1
                # 빈칸을 만날 때만 바이러스가 퍼지는 경우이므로, 이 경우에서만 생각해준다.
                # (바이러스 활성화는 엄밀히 말하면 바이러스가 퍼지는게 아니라, 활성화만 시켜주는 것이다)
                if new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = 2
                    last_cnt = cnt + 1
                q.append((nx, ny, cnt + 1))
    #print(2)
    flag=0

    for x in range(n):
        count = new_arr[x].count(0)
        if count>0:
            flag=1
            break
    if flag ==1:
        continue


    result = min(result,last_cnt)

if result==1e9:
    print(-1)
else:
    print(result)






