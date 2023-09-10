n = int(input())
k = int(input())
#상좌하우
dx = [-1,0,1,0]
dy = [0,-1,0,1]
apple = []
for _ in range(k):
    apple.append(list(map(int,input().split())))
map = [[0]*n for _ in range(n)]
for i in apple:
    x,y = i
    x=x-1
    y=y-1
    map[x][y] = 2
time = {}
l = int(input())
for _ in range(l):
    i,j = input().split()
    time[int(i)] = j
cnt = 0
###사과 있으면 2 이고 뱀의 현재위치 1로 표기
x,y= 0,0
from collections import deque
snake = deque()
snake.append((0,0))
#초기값 오른쪽으로 이동
d = 3
while True:
    #### 멈추는 조건 체크
    #### 1. 벽에 닿거나
    #### 2. 뱀이 뱀의 몸에 닿거나
    cnt+=1




    nx = x+dx[d]
    ny = y+dy[d]

    if nx >=n or nx <0 or ny >= n or ny <0 :
        break
    if (nx,ny) in snake:
        break
    ## 사과 먹으면
    if map[nx][ny] ==2 :
        snake.append((nx,ny))
        ##사과 없어짐
        map[nx][ny]=0
    elif map[nx][ny] ==0:
        #머리이동
        snake.append((nx,ny))
        #꼬리도 이동
        snake.popleft()
    if cnt in time.keys():
        if time[cnt] == 'D':
            d = (d-1)%4
        elif time[cnt] == 'L':
            d = (d+1)%4


    (x,y) = (nx,ny)




print(cnt)


