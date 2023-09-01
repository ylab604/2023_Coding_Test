n,l = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

#행
visited1=[[0]*n for _ in range(n)]
#열
visited2=[[0]*n for _ in range(n)]
cnt=0
"""
1. 높이차이가 1이난다 => 경사로 놓을 수 있는지 체크
경사로 

2. 더 많이 난다 => 경사로 놓지 못함

3. 모두 높이가 같으면 카운트
"""
#행
for i in range(n):
    check=0
    equal=0
    #행이 모두 같을때
    for j in range(n-1):
        if arr[i][j]==arr[i][j+1]:
            equal=1
        else:
            equal=0
            break

    if equal==1:
        cnt+=1
        continue



    for j in range(n-1):
        #2이상이면 컷
        if abs(arr[i][j] - arr[i][j + 1]) >= 2:
            check=0
            break
        #왼쪽이 클때
        if arr[i][j]-arr[i][j+1] ==1:
            #오른쪽에서 길이 l만큼의 같은 높이의 칸이 있는지 확인해야함
            #범위를 넘어가지 않는다면
            if j+l <n:
                #높이가 같다면
                flag=0
                for k in range(l):
                   if arr[i][j+1]==arr[i][j+1+k] and visited1[i][j+1+k]==0:
                       flag=1
                   else:
                       flag=0
                       break
                if flag==1:
                    check=1
                    #방문체크
                    for k in range(l):
                        visited1[i][j+1+k]=1
                else:
                    check=0
                    break

            else:
                # 범위 넘어간더면
                check = 0
                break
        #오른쪽이 클때
        elif arr[i][j]-arr[i][j+1]==-1:
            #왼쪽에 길이 l만큼이 있는지 확인
            if j+1-l>=0:
                flag=0
                for k in range(l):
                    if arr[i][j]==arr[i][j-k] and visited1[i][j-k]==0:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    check = 1
                    # 방문체크
                    for k in range(l):
                        visited1[i][j-k] = 1
                else:
                    check = 0
                    break
            else:
                # 범위 넘어간더면
                check = 0
                break



    if check==1:
        cnt+=1





#열
for j in range(n):
    check=0
    equal=0
    # 열이 모두 같을때
    for i in range(n - 1):
        if arr[i][j] == arr[i+1][j]:
            equal = 1
        else:
            equal=0
            break

    if equal == 1:
        cnt += 1
        continue



    for i in range(n-1):
        # 2이상이면 컷
        if abs(arr[i+1][j] - arr[i][j]) >= 2:
            check = 0
            break
        # 위쪽이 클때
        if arr[i][j] - arr[i+1][j] == 1:
            # 오른쪽에서 길이 l만큼의 같은 높이의 칸이 있는지 확인해야함
            # 범위를 넘어가지 않는다면
            if i + l < n:
                # 높이가 같다면
                flag = 0
                for k in range(l):
                    if arr[i+1][j] == arr[i+1+k][j ] and visited2[i+ 1 + k][j ] == 0:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    check = 1
                    # 방문체크
                    for k in range(l):
                        visited2[i + 1 + k][j] = 1
                else:
                    check = 0
                    break
            else:
                #범위 넘어간더면
                check=0
                break
        # 아래쪽이 클때
        elif arr[i][j] - arr[i+1][j] == -1:
            # 위쪽에 길이 l만큼이 있는지 확인
            if i+1 - l >= 0:
                flag = 0
                for k in range(l):
                    if arr[i][j] == arr[i-k][j] and visited2[i-k][j] == 0:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    check = 1
                    # 방문체크
                    for k in range(l):
                        visited2[i-k][j] = 1
                else:
                    check = 0
                    break
            else:
                # 범위 넘어간더면
                check = 0
                break

    if check == 1:
        cnt += 1

print(cnt)