import math


def solution(n, k):
    ####k진법으로 만들기####
    tmp = ""
    while 1:
        a = n % k
        tmp += str(a)
        n = n // k
        if n == 0:
            break

    # tmp의 역수가 k진수
    tmp = tmp[::-1]
    # 0을기준으로 나누어주고
    # tmp="1100010"
    split = tmp.split("0")

    answer = []
    for i in split:
        if i != "1" and i != "":
            answer.append(i)
    # print(answer)
    result = 0
    ##소수 판별
    for j in answer:
        flag = 1

        for x in range(2, int(math.sqrt(int(j))) + 1):
            if int(j) % x == 0:
                flag = 0
                break

        if flag == 1:
            result += 1

    return result