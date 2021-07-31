t=int(input())
for c in range(0,t):
    i_p=input().split()
    speed=1
    for i in i_p:
        speed=speed*float(i)
    result=100/speed
    if result<9.576:
        print('Yes')
    elif result>=9.576:
        print('No')
