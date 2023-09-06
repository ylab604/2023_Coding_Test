## 모든 노드의 가중치 값의 합이 0이면 가능 아니면 -1 리턴
## 어디를 노드의 시작점이라고 해도 상관이 없음 어짜피 다 연결되어있음
## 모든 노드의 가중치의 합이 0 안되면 -1


from collections import deque


def bfs(a, edges):
    dic = {}
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        if v1 not in dic.keys():
            dic[v1] = []
        if v2 not in dic.keys():
            dic[v2] = []
        dic[v1].append(v2)
        dic[v2].append(v1)

    q = deque([(-1, 0)])
    path = []
    visited = [0] * len(a)
    visited[0] = 1
    while q:
        p, c = q.popleft()
        path.append((p, c))

        des = dic[c]

        if des:
            for d in des:
                if not visited[d]:
                    q.append((c, d))
                    visited[d] = True

    return path[::-1]


def solution(a, edges):
    answer = 0
    path = bfs(a, edges)

    for parent, child in path[:-1]:
        weight = a[child]
        answer += abs(weight)
        a[parent] += weight

    if a[0] == 0:
        return answer

    else:
        return -1

    return answer