import random

t_c=int(input())
for t in range(1,(t_c+1)):
    n_c=input()
    temp_n_c=n_c.split()
    n=int(temp_n_c[0])
    c=int(temp_n_c[1])
    #a_l=permutations([1,2,3,4,5,6,7,8,9], n)
    
    a=[]
    for p in range(0,n):
        a.append(random.randint(0,99))
        s-=1
    
    while val!=c:
        
        a_t=[]
        a_t.extend(l)
        a=a_t.copy()
        val=0
        #print(a)
        for i in range(0,n-1):
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
        if val==c:
            break
        #print(val)
        val=-1
    res=''
    for r in l:
        res=res+' '+str(r)
    if val==c:
        print('case #'+str(t)+':'+res)
    elif val==-1:
        print('case #'+str(t)+':'+' IMPOSSIBLE')
