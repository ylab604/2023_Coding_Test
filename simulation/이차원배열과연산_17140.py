##fix

r,c,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]

def calR():
    global arr
    new_graph=[]
    for i in arr:
        element  = set(i)
        tmp = [] #(원소, 갯수)
        tmp2=[] #새로운행
        for j in element:
            if j==0:
                continue
            cnt = i.count(j)
            tmp.append((j,cnt))

        tmp.sort(key = lambda x:(x[1],x[0]))

        for l in tmp:
            tmp2.append(l[0])
            tmp2.append(l[1])

        tmp2 = tmp2[:100] #100개 제한

        new_graph.append(tmp2)

    max_len = max(map(len,new_graph))

    #빈칸은 0만큼
    for i in range(len(new_graph)):
        while len(new_graph[i]) != max_len:
            new_graph[i].append(0)
    ##update arr
    arr = new_graph
for i in range(101):
    try:
        if arr[r-1][c-1]==k:
            print(i)
            break
    except:
        pass


    if len(arr[0])>len(arr):
        arr=list(map(list,zip(*arr)))
        calR()
        arr = list(map(list,zip(*arr)))
    else:
        calR()
else:
    print(-1)

