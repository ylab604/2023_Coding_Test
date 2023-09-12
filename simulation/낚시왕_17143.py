from copy import deepcopy
#d가 1 위 2 아래 3 오른쪽 4 왼쪽
dx=[-1,1,0,0]
dy=[0,0,1,-1]
r,c,m = map(int,input().split())



fish = [[[0]]*c for _ in range(r)]
for _ in range(m):
    R,C,s,d,z = map(int,input().split())
    fish[R-1][C-1]=[s,d,z]
cnt=0
#상어 크기의 합
fish_cnt=0
while True:
    cnt+=1
    tmp = [[[0]]*c for _ in range(r)]
    if cnt==c+1:
        break
    ##땅에 가장 가까운거 잡기 잡으면 사라짐
    for i in range(r):

        if fish[i][cnt - 1] != [0]:
            fish_cnt += fish[i][cnt - 1][2]
            fish[i][cnt - 1] = [0]
            # 한마리만 잡아
            break


    ##상어 이동
    for i in range(r):
        for j in range(c):
            if fish[i][j] != [0]:
                #디렉션 체크, 속도체크 // 속력, 방향, 크기 // s,d,z
                d = fish[i][j][1]
                nx = i + dx[d-1]*fish[i][j][0]
                ny = j + dy[d-1]*fish[i][j][0]
                ##범위 넘어갔을경우와 아닐경우 체크
                if nx >=0 and nx<r and ny>=0 and ny<c:
                    if tmp[nx][ny] ==[0]:
                        tmp[nx][ny] = fish[i][j]
                    elif tmp[nx][ny] !=[0]:
                        if tmp[nx][ny][2] > fish[i][j][2]:
                            pass
                        elif tmp[nx][ny][2] < fish[i][j][2]:
                            tmp[nx][ny] = fish[i][j]
                #범위 벗어 났을 경우
                else:
                    #한개씩 체크
                    #nx = i + dx[d - 1]
                    nx=i
                    #ny = j + dy[d - 1]
                    ny=j
                    if d ==1 or d==2:
                        k = (fish[i][j][0])%(2*r-2)

                    else:
                        k = (fish[i][j][0]) % (2*c-2)
                    for _ in range(k):
                        nx = nx + dx[d - 1]
                        ny = ny + dy[d - 1]

                        #범위 벗어났다면
                        if nx<0 or nx >=r or ny<0 or ny>=c:
                            ##원상태 복귀
                            nx = nx - dx[d - 1]
                            ny = ny - dy[d - 1]
                            if d ==1 :
                                d =2
                            elif d==2:
                                d=1
                            elif d==3:
                                d=4
                            elif d==4:
                                d=3
                            ##반대방향 마저 가기
                            nx = nx + dx[d - 1]
                            ny = ny + dy[d - 1]
                    ##방향업데이트
                    fish[i][j][1] = d
                    #루프끝났다면
                    if tmp[nx][ny] == [0]:

                        tmp[nx][ny] = fish[i][j]
                    elif tmp[nx][ny] != [0]:
                        if tmp[nx][ny][2] > fish[i][j][2]:
                            pass
                        elif tmp[nx][ny][2] < fish[i][j][2]:
                            tmp[nx][ny] = fish[i][j]


    #fish 업데이트
    fish= deepcopy(tmp)


print(fish_cnt)