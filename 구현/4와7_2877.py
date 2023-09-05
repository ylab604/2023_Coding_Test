k= int(input())
n =1
c =2
while k >c :
    n+=1
    c+=2**n

x=k-(c-2**n)-1
#카운트 0부터 하기 위해 -1 추가


print(bin(x).lstrip('0b').zfill(n).replace('0','4').replace('1','7'))

