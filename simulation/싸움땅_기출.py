N,M,K = map(int,input().split())
gunBoard = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        if row[j] ==0:
            continue
        gunBoard[i][j].append(row[j])

playerList = list()
playersBoard = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(M):
    x,y,d,s = map(int,input().split())
    playerList.append([x-1,y-1,d,s,0])
    playersBoard[x-1][y-1] = i

scores = [0]*M

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def rotateDirection(d):
    if d+1<4:
        return d+1
    return 0
def flipDirection(d):
    d = (d+2)%4
    return d
def isVaild(nx,ny):
    return 0<=nx<N and 0<=ny<N

def getMoveCoordinate(i):
    x,y = playerList[i][0],playerList[i][1]
    nx,ny = x+dx[playerList[i][2]],y+dy[playerList[i][2]]
    #격자안에 없으면
    if not isVaild(nx,ny):
        playerList[i][2] = flipDirection(playerList[i][2])
        nx,ny = x+dx[playerList[i][2]],y+dy[playerList[i][2]]
    return nx,ny
def move(playerIndex,nx,ny):
    x,y = playerList[playerIndex][0],playerList[playerIndex][1]
    #초기화
    playersBoard[x][y]=-1
    playersBoard[nx][ny] = playerIndex
    playerList[playerIndex][0],playerList[playerIndex][1] = nx,ny
    return
def getGun(playerIndex,nx,ny):
    if playerList[playerIndex][4] ==0:
        playerList[playerIndex][4] =max(gunBoard[nx][ny])
        gunBoard[nx][ny].pop(gunBoard[nx][ny].index(max(gunBoard[nx][ny])))
    else:
        maxGun = max(gunBoard[nx][ny])
        playerGun = playerList[playerIndex][4]
        if playerGun >=maxGun:
            return
        playerList[playerIndex][4] = max(gunBoard[nx][ny])
        gunBoard[nx][ny][gunBoard[nx][ny].index(max(gunBoard[nx][ny]))] = playerGun
    return

def fight(player1Index, player2Index):
    if playerList[player1Index][3] + playerList[player1Index][4] > playerList[player2Index][3] + playerList[player2Index][4]:
        return player1Index, player2Index, abs(playerList[player1Index][3] + playerList[player1Index][4] - playerList[player2Index][3] - playerList[player2Index][4])
    elif playerList[player1Index][3] + playerList[player1Index][4] < playerList[player2Index][3] + playerList[player2Index][4]:
        return player2Index, player1Index, abs(playerList[player1Index][3] + playerList[player1Index][4] - playerList[player2Index][3] - playerList[player2Index][4])
    else:
        if playerList[player1Index][3] > playerList[player2Index][3]:
            return player1Index, player2Index, abs(playerList[player1Index][3] + playerList[player1Index][4] - playerList[player2Index][3] - playerList[player2Index][4])
        else:
            return player2Index, player1Index, abs(playerList[player1Index][3] + playerList[player1Index][4] - playerList[player2Index][3] - playerList[player2Index][4])

def dropAllGuns(playerIndex,nx,ny):
    gunBoard[nx][ny].append(playerList[playerIndex][4])
    playerList[playerIndex][4]=0
def getLoserMovement(i):
    x,y = playerList[i][0],playerList[i][1]
    nx,ny = x+dx[playerList[i][2]],y+dy[playerList[i][2]]
    while not (isVaild(nx,ny) and playersBoard[nx][ny]==-1):
        playerList[i][2] = rotateDirection(playerList[i][2])
        nx,ny = x+dx[playerList[i][2]],y+dy[playerList[i][2]]
    return nx,ny

def play():
    for i in range(M):
        nx,ny = getMoveCoordinate(i)
        if playersBoard[nx][ny] == -1:
            if len(gunBoard[nx][ny]) ==0:
                move(i,nx,ny)
                continue
            getGun(i,nx,ny)
            move(i,nx,ny)
        else:
            winnerIndex,loserIndex,socreDiff = fight(i, playersBoard[nx][ny])
            scores[winnerIndex]+=socreDiff
            move(i,nx,ny)
            ##진플레이어
            dropAllGuns(loserIndex,nx,ny)
            lx,ly = getLoserMovement(loserIndex)
            move(loserIndex,lx,ly)
            if len(gunBoard[lx][ly])!=0:
                getGun(loserIndex,lx,ly)
            ##이긴플레이어
            getGun(winnerIndex,nx,ny)
            playersBoard[nx][ny] = winnerIndex
    return
for _ in range(K):
    play()
for i in scores:
    print(i,end=" ")