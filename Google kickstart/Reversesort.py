t_c=int(input())
for t in range(1,(t_c+1)):
    #print(t)
    n_c=int(input())
    a_s=input()
    temp_a=a_s.split()
    a=[]
    for e in temp_a:
        a.append(int(e))
    #print(a)
    val=0
    for i in range(0,n_c-1):
        a_ca=a[i:]
        a_cal=a_ca.copy()
        mi=min(a_cal)
        j=a.index(mi)
        a_re=a[i:(j+1)]
        a_rev=a_re[::-1]
        index=i
        #print(a_re)
        for e in a_rev:
            a[index]=e
            index+=1            
        val+=(j-i+1)
    print('case #'+str(t)+': '+str(val))
