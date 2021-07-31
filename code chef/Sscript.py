T=int(input())
for c in range(1,T+1):
    i_p_N_K=input().split()
    K=int(i_p_N_K[1])
    S=input()
    count=0
    result_l=[]
    condition=False
    for i in S:
        if i!='*':
            if count>=K:
                condition=True
                break
            count=0
        elif i=='*':
            count+=1
        if count>=K:
            condition=True
            break
    if condition:
        print('Yes')
    else:
        print('No')
