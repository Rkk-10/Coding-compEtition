T=int(input())
for c in range(1,T+1):
    i_p_N_M_K=input().split()
    N=int(i_p_N_M_K[0])
    A=[]
    for i in range(0,N):
        t=input().split()
        a=[int(b) for b in t]
        A.append(a.copy())
    print(A.count(4))
    
