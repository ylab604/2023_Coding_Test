import copy
n,m,r = map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

#r만큼 회전하자
for _ in range(r):
    #외부에서 안으로 들어가자 결국엔 행과 열중 작은 곳의 반만 구현하면 되므로!!
    #직접 몇개 그려서 체크해보자
    for i in range(min(n,m)//2):
        x, y = i,i
        f_value = graph[x][y]
        #배열의 왼쪽
        for j in range(i+1,n-i):
            x = j
            tmp = graph[x][y]
            graph[x][y]=f_value
            f_value = tmp
        #아래
        for j in range(i+1,m-i):
            y = j
            tmp = graph[x][y]
            graph[x][y] = f_value
            f_value = tmp
        #오른쪽
        for j in range(i+1,n-i):
            x=n-j-1
            tmp = graph[x][y]
            graph[x][y]=f_value
            f_value = tmp

        #위
        for j in range(i+1,m-i):
            y = m-j-1
            tmp = graph[x][y]
            graph[x][y]=f_value
            f_value = tmp

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()


