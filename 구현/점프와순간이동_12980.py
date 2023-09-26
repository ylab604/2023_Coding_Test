def solution(n):
    ans = 0
    #순간이동을 많이하면 되는게 포인트
    #순간이동은 짝수에 할 수 있음
    while True:
        if n==0:
            break
        if n%2==0:
            #짝수면 그냥넘어가
            n=n//2
        elif n%2 !=0:
            #홀수면 빼주고 ans+=1
            n -=1
            n=n//2
            ans+=1

    return ans