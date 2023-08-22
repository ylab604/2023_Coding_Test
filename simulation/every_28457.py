#보드크기 n, 시작 돈 S, 월급 W, 황금열쇠 카드의 개수 G
n,S,W,G = map(int,input().split())
marble={}
gold_key=[]
gold_key_cnt=0
visited = [0]*(4*n-4)
for _ in range(G):
    gold_key.append(list(map(int,input().split())))

for i in range(4*n-4):
    #특수칸
    if i==0:
        marble[i+1]=['start']
        visited[i]=1
    elif i==n-1:
        marble[i+1]=['mu']
        visited[i] = 1
    elif i==2*n-1-1:
        marble[i+1]=['sa']
        visited[i] = 1
    elif i == 3*n-2-1:
        marble[i+1]=['space']
        visited[i] = 1
    #일반칸
    else:
        #나중에 정수처리 필수
        marble[i+1]=(input().split())
I=int(input())
dice=[]
for _ in range(I):
    dice.append(list(map(int,input().split())))

### 카운트  1부터 시작
## 두주사위의 합이 12가 최대고, n은 3부터 시작이므로(8칸) -로 계산하기보다는
## 몫과 나머지로 계산하는거 낫다!!
cnt=1
##계좌에 남아있는돈
cash=S
##사회복지기금
gibu=0


def move(cnt, go_num ,cash, gibu,n,W):
    cnt+=go_num

    if cnt>4*n-4:
        a=cnt//(4*n-4)
        b=cnt%(4*n-4)
        cnt=b
        cash+=W*a
    else:
        pass

    return cnt, cash, gibu

def G_fuction (num,cash,gibu,gold_cnt,cnt,n,W,flag,visited,win):

    if num ==1:
        cash+=gold_key[gold_cnt][1]
    elif num ==2:
        if cash>=gold_key[gold_cnt][1]:
            cash-=gold_key[gold_cnt][1]
        else:
            win=1
            #exit(0)
    elif num ==3:
        if cash>=gold_key[gold_cnt][1]:
            cash-=gold_key[gold_cnt][1]
            gibu+=gold_key[gold_cnt][1]
        else:
            win=1
            #exit(0)


    elif num ==4:
        cnt, cash, gibu=move(cnt, gold_key[gold_cnt][1],cash,gibu,n,W)
        if marble[cnt][0] =='mu':
            flag=1

        #사회복지
        elif marble[cnt][0] =='sa':
            cash+=gibu
            #기부금 초기화
            gibu=0

        #우주선
        elif marble[cnt][0] =='space':
            #스타트 시작 및 월급 추가
            cnt=1
            cash+=W

        elif marble[cnt][0] =='L':
            if visited[cnt-1]==0 and cash >= int(marble[cnt][1]):
                cash-=int(marble[cnt][1])
                visited[cnt-1]=1
            else:
                pass

    return cash, gibu, cnt, flag,win
#무인도 체크
flag=0
cnt_mu=0
win=0
##시작 (cnt=1 부터 하는 것을 명심!!)
for x,y in dice:
    go_num = x + y
    #무인도에 갇힌 상태
    if flag==1:
        #같은 수면 다음 수에 나간다.
        if x==y or cnt_mu==3:
            flag=0
            cnt_mu=0
        else:
            cnt_mu+=1
    else:
        cnt, cash, gibu = move(cnt, go_num, cash, gibu, n, W)
        #무인도
        if marble[cnt][0] =='mu':
            flag=1

        #사회복지
        elif marble[cnt][0] =='sa':
            cash+=gibu
            #기부금 초기화
            gibu=0

        #우주선
        elif marble[cnt][0] =='space':
            #스타트 시작 및 월급 추가
            cnt=1
            cash+=W

        elif marble[cnt][0] =='start':
            pass

        elif marble[cnt][0] =='G':


            if gold_key_cnt<G:
                cash, gibu, cnt,flag,win = G_fuction(gold_key[gold_key_cnt][0], cash, gibu, gold_key_cnt, cnt, n, W,flag,visited,win)

                gold_key_cnt+=1
                if win==1:
                    print('LOSE')
                    exit(0)
            else:
                gold_key_cnt=0

                cash, gibu, cnt, flag,win = G_fuction(gold_key[gold_key_cnt][0], cash, gibu, gold_key_cnt, cnt, n, W, flag,
                                                  visited,win)
                gold_key_cnt += 1
                if win==1:
                    print('LOSE')
                    exit(0)
        #땅들 돈있으면 사야되고 없으면 pass
        elif marble[cnt][0] =='L':
            if visited[cnt-1]==0 and cash >= int(marble[cnt][1]):
                cash-=int(marble[cnt][1])
                visited[cnt-1]=1
            else:
                pass

if sum(visited)==4*n-4-G:
    print("WIN")
else:
    print("LOSE")



