## 접근
"""우연히도 팀이 짝수로 구성되어있고 인원도 짝수이다.
즉, 모든 경우의수를 고려하되 check 해야하는 대상이
전체 수의 N/2되면 된다. 이를 dfs 백트레킹을 통하여
경우의 수를 확인한다."""

n=int(input())
score = []

for _ in range(n):
    score.append(list(map(int,input().split())))

def dfs(depth,idx):
    global diff
    if depth==n//2:
        score1,score2=0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    score1+=score[i][j]
                elif not visited[i] and not visited[j]:
                    score2+=score[i][j]
        diff = min(diff,abs(score1-score2))
        return
    for i in range(idx,n):
        if not visited[i]:
          visited[i]=True
          dfs(depth+1,i+1)
          visited[i]=False


visited = [False for _ in range(n)]
diff = int(1e9)
dfs(0,0)
print(diff)