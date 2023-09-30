# BOJ_G3_23288_주사위 굴리기 2[2023-09-30]
https://www.acmicpc.net/problem/23288

<접근법>
```
0. 구현 + bfs
1. 디버깅 시간을 많이 벌기
```



```python
from collections import deque

#좌상우하
dx=[0,-1,0,1]
dy=[-1,0,1,0]
n,m,k = map(int,input().split())
arr=[]
dice=[2,1,5,6,4,3]
for _ in range(n):
    arr.append(list(map(int,input().split())))
#초기 방향 설정 동쪽
d = 2
x,y = 0,0
score=0
for i in range(k):
    ##다음으로 이동
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        pass
    else:
        d += 2
        d %= 4
        nx = x + dx[d]
        ny = y + dy[d]



    #nx,ny=x,y


    ###위로 움직이면
    tmp=dice[:]
    if d==1:
        #up
        dice=[tmp[1],tmp[2],tmp[3],tmp[0],tmp[4],tmp[5]]
    elif d==3:
        #down
        dice=[tmp[3],tmp[0],tmp[1],tmp[2],tmp[4],tmp[5]]
    elif d==2:
        #right
        dice=[tmp[0],tmp[4],tmp[2],tmp[5],tmp[3],tmp[1]]
    elif d==0:
        #left
        dice=[tmp[0],tmp[5],tmp[2],tmp[4],tmp[1],tmp[3]]

    ####check the score
    q=deque()
    visited=[[0]*m for _ in range(n)]
    ##
    q.append((nx,ny))
    ##방문체크
    visited[nx][ny] = 1
    while q:
       na,nb=q.popleft()
       for i in range(4):
            nc=na+dx[i]
            nd=nb+dy[i]
            ##범위안에 있으면
            if 0<=nc<n and 0<=nd<m:
                ## 숫자 같으면
                if arr[nc][nd] == arr[nx][ny]:
                    if visited[nc][nd]==0:
                        visited[nc][nd]=1
                        q.append((nc,nd))
    #score연산
    for a in visited:
        score=score+sum(a)*arr[nx][ny]

    # A>B이면 +1
    if dice[3] > arr[nx][ny]:
        d += 1
        d %= 4

    # A<B이면 -1
    elif dice[3] < arr[nx][ny]:
         d -= 1
         d %= 4

    else:
            ##그대로진행
        pass
    x,y = nx,ny


print(score)






```