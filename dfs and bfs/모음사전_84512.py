cnt = 0
def solution(word):
    a = ["A", "E", "I", "O", "U"]
    b = []
    c = {}
    def dfs(depth, b):
        global cnt
        if depth == 5:
            return
        for i in range(5):
            b.append(a[i])
            cnt += 1
            c[''.join(b)] = cnt
            dfs(depth + 1, b)
            b.pop()
    dfs(0, b)
    answer = c[word]
    return answer