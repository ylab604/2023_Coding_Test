#8칸
#상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
n,m,k = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

tree=[]
for _ in range(m):
    tree.append(list(map(int,input().split())))

grd =[[[5] for _ in range(n)] for _ in range(n)]

#트리 위치 세팅
for i in tree:
    x,y,a = i
    grd[x-1][y-1].append([a])

#### 봄여름가을겨울 조건 코드
#### k년 후 체크

###봄
###나무가 여러개 있으면 나이가 어린 나무부터 나이+=1
###자신의 나이만큼 양분을 섭취하고 나이+=1
###만약 섭취할 양분이 부족하면 나무 죽음

for _ in range(k):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #나무 체크
            if len(grd[i][j]) !=1:
                #나이 어린것부터 양분섭취 후 나이+=1
                grd[i][j][1].sort()
                #print(len(grd[i][j]))
                for z in range(len(grd[i][j][1])):
                    #print(grd[i][j][1])
                    #print(z)

                    if grd[i][j][0] >= grd[i][j][1][z]:
                        #나이만큼 빼주고
                        grd[i][j][0]-=grd[i][j][1][z]
                        #나이증가
                        grd[i][j][1][z]+=1
                    #여름
                    #만약 양분부족하다면? 여름에 나무죽고 나이를 2로 나눈값이
                    #나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
                    else:
                    ######################################
                        #양분준거 빼고 죽음
                        alpha = grd[i][j][1][z:]
                        grd[i][j][1]=grd[i][j][1][:z]
                        #print(grd[i][j][1][:z])
                        #죽은나무들 양분됨
                        #print(grd[i][j][1][:])
                    ######################################
                        #print(alpha)
                        for l in alpha:
                            grd[i][j][0]+=l//2
                        if len(grd[i][j][1])==0:
                            #빈칸이면 빈칸 삭제
                            del(grd[i][j][1])
                        break
            # 가을
            # 나무가 번식한다.
            if len(grd[i][j]) != 1:
                #print(grd[i][j])
                for leaf in grd[i][j][1]:
                    #5의배수라면
                    if leaf%5==0:
                        #8방향에 나무심기
                        for num in range(8):
                            nx= i+dx[num]
                            ny= j+dy[num]
                            if 0<=nx<n and 0<=ny<n:
                                tmp[nx][ny]+=1


            #겨울
            #양분주기
            grd[i][j][0]+=arr[i][j]
    ###### 나무심기
    for i in range(n):
        for j in range(n):
            #나무칸 없다면
            if len(grd[i][j]) ==1 and tmp[i][j] !=0:
                flag=0
                for q in range(tmp[i][j]):
                    if flag==1:
                        break
                    grd[i][j].append([1])
                    flag=1
                #초기화
                flag=0
                for e in range(tmp[i][j]-1):
                    grd[i][j][1].append(1)
                #print(1111111)
            elif len(grd[i][j]) !=1 and tmp[i][j] !=0:
                #print(grd[i][j][1])
                for w in range(tmp[i][j]):
                    grd[i][j][1].append(1)

##check
result=0
for i in range(n):
    for j in range(n):
        if len(grd[i][j]) !=1:
           result+= len(grd[i][j][1])
print(result)
