##경우의수##
# 나머지가 6이상
# 5이면서 앞자리가 5이상일때
# 5이하일때
def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10

        if n >= 6:
            storey += 10 - n
            answer += 10 - n

        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n
            answer += 10 - n

        else:
            answer += n
        storey = storey // 10


    return answer
