from collections import deque
from collections import Counter
n,k = map(int,input().split())
#2차원으로 풀자
arr=[[0]*2 for _ in range(2*n)]

a= list(map(int,input().split()))

for i in range(len(a)):
    arr[i][0]=a[i]
##내구도, 로봇 유무
##오른쪽 rotate 확인
q= deque(arr)
cnt=1
while True:
    #1. 벨트가 각 칸위에 있는 로봇과 함께 한 칸 회전한다.
    q.rotate(1)
    #2. 가장 먼저 벨트에 올라간 로봇부터 이동
    #2-1. 앞에 로봇 없고 그칸의 내구도가 1이상 남아야
    ##### 사실상 로봇은 n번칸 그리고 즉시 내림 #####
    ##n번칸 로봇내려
    if q[n - 1][1] == 1:
        q[n - 1][1] = 0
    for i in range(n-1,-1,-1):
        if q[i][1] ==1:
            if q[i+1][1] ==0 and q[i+1][0] !=0:
                q[i][1]=0
                q[i+1][0]-=1
                q[i+1][1]=1


    ##n번칸 로봇내려
    if q[n-1][1] ==1:
        q[n-1][1]=0
    #print(q[n-1][1])
    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇올리기
    if q[0][0] !=0:
        q[0][1]=1
        q[0][0]-=1
    result =0
    for j in q:
        if j[0]==0:
            result+=1
    if result>=k:
        break
    cnt+=1
print(cnt)

