# 카드 매개변수를 이미 줬기 때문에 문제가 요구한 사항을 구현하면된다.
# 조건은 얻을 수 있는 가장 큰수 => 상자의 경우수 구한다음 정렬해서 곱하기
def solution(cards):
    answer = []
    visited = [0] * len(cards)
    for i in cards:

        if visited[i - 1] != 1:
            tmp = []
            # 만날 때 까지
            while i not in tmp:
                # 방문처리
                visited[i - 1] = 1
                tmp.append(i)
                i = cards[i - 1]
                print(tmp)

            answer.append(len(tmp))
    answer.sort(reverse=True)
    if len(answer) == 1:
        result = 0
    else:
        result = answer[0] * answer[1]

    return result
