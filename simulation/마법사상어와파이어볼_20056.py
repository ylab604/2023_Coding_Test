n,m,k=map(int,input().split())
#방향
#상 우상 우 우하 하 좌하 좌 좌상
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
from copy import deepcopy
#n바이n격자 m개 파이어볼, k번 이동
#r,c,질량m,속도s,방향d
info=[]
for _ in range(m):
    r,c,m,s,d = map(int,input().split())
    info.append((r-1,c-1,m,s,d))

##arr 만들기
arr=[[0]*n for _ in range(n)]
###초기 지도 셋팅 리스트로 받아서 어팬드 가능하고 len추출 가능하게
#print(arr)
for i in info:
    arr[i[0]][i[1]] = [[i[2],i[3],i[4]]]
#print(arr)
#마법사의 이동시키기
#k번 이동함
for _ in range(k):
    #1 모든 파이어볼이 자신의 방향으로 s만큼이동
    new_arr=[[0]*n for _ in range(n)]
    ##안에들어있는거 기준으로 하자
    for i in range(n):
        for j in range(n):
            if arr[i][j] !=0:
                #한개만 있다면
                if len(arr[i][j]) ==1:
                    #print(arr[i][j])

                    nx = (i+dx[arr[i][j][0][2]]*arr[i][j][0][1])%n
                    ny = (j+dy[arr[i][j][0][2]]*arr[i][j][0][1])%n
                    if new_arr[nx][ny]==0:
                        new_arr[nx][ny]=arr[i][j]
                    else: new_arr[nx][ny].append(arr[i][j][0])

                else:
                    #여러개 이동시켜야함
                    for v in arr[i][j]:
                        #v[0], v[1], v[2] 질량 속도 방향
                        nx = (i+dx[v[2]]*v[1])%n
                        ny = (j + dy[v[2]] * v[1]) % n
                        if new_arr[nx][ny] == 0:
                            new_arr[nx][ny] = [v]
                        else:
                            new_arr[nx][ny].append(v)
    # 이동시켰으니 2개이상인 곳은 4개로 분열시켜야됨 분열만 시키고 다음턴으로 넘김
    #m,s,d
    #print(arr[i][j])
    #print(new_arr)
    for i in range(n):
        for j in range(n):
            if new_arr[i][j] !=0:
                if len(new_arr[i][j]) !=1:
                    ##일단 합치기
                    a,b,f =0,0,0
                    #print(new_arr)
                    for case in new_arr[i][j]:
                        #print(case)
                        ######a,b,f 질량 속도 방향
                        a+=case[0]
                        b+=case[1]
                        if case[2] in [0,2,4,6]:
                            f+=1
                        elif case[2] in [1,3,5,7]:
                            f+=0
                    if f == 0 or f==len(new_arr[i][j]):
                        d1,d2,d3,d4 = 0,2,4,6
                    else:
                        d1,d2,d3,d4 = 1,3,5,7
                    a=a//5
                    b = b // len(new_arr[i][j])
                    if a!=0:
                    #4개로 분열하기
                        new_arr[i][j] = [[a,b,d1],[a,b,d2],[a,b,d3],[a,b,d4]]
                    else:
                        #없애기
                        new_arr[i][j]=0
    ###arr업데이트
    arr = deepcopy(new_arr)

### 질량 세기
cnt=0
#print(arr)
for i in range(n):
    for j in range(n):

        if arr[i][j] !=0:
            #print(arr[i][j])
            if len(arr[i][j]) ==1:
                cnt+=arr[i][j][0][0]
            else:
                for v in arr[i][j]:
                    #print(v)
                    cnt+=v[0]
print(cnt)






