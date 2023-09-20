import collections
answer = []
#seller_dic = collections.defaultdict(int)   # 판매자 - 돈 총량
enroll_dic = collections.defaultdict(str)  # 자식 노드 - 부모 노드
answer_dic = collections.defaultdict(int)   # 전체 인원 - 이익 분배 후 돈 총량

def give_money(now, now_money):
    if now == "-" or now_money < 1:
        return

    answer_dic[now] += now_money - (now_money // 10)
    give_money(enroll_dic[now], (now_money // 10) )

def solution(enroll, referral, seller, amount):

    for i in range(len(enroll)):
        enroll_dic[enroll[i]] += referral[i]

    for i in range(len(seller)):
        give_money(seller[i], amount[i] * 100)

    for i in range(len(enroll)):
        answer.append(answer_dic[enroll[i]])

    return answer