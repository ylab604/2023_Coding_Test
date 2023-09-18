def solution(id_list, report, k):
    report = set(report)
    report = list(report)
    answer = []
    check = {}
    result = {}
    # 누가 누구 신고했는지 확인해야함
    # 그리고 그게 k가 넘으면 answer에 반환

    for i in report:
        # x가 y를 신고 일단 y가 신고당한거 확인하는 딕셔너리 생성
        x, y = i.split()

        if y in check.keys():
            check[y] += 1
        else:
            check[y] = 1

        if x in result.keys():
            result[x].append(y)

        else:
            result[x] = [y]

    for i in id_list:
        cnt = 0
        # print(1)
        if i in result.keys():
            # print(1)
            for j in result[i]:

                if check[j] >= k:
                    cnt += 1

            answer.append(cnt)
        else:
            answer.append(cnt)

    return answer