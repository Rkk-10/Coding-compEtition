from itertools import combinations 
t_c=int(input())
for t in range(1,(t_c+1)):
    n_c=input().split()
    X=int(n_c[0])
    Y=int(n_c[1])
    s=n_c[2]
    count=s.count('?')
    cost_l=[]
    p=['C','J']
    if count>2:
        cc=count-2
        for i in range(0,cc):
            p.append(p[i])
    combi=combinations(p, count)
    for comb in combi:
        
        co=[]
        co.extend(comb)
        s_c=s
        print('co')
        print(co)
        a=True
        while a:
            
            try:
                #i=s_c.index('?')
                s_c.replace('?',co.pop(),1)
            except:
                a=False
        print(s_c)
        #i=0
        cost=0
        while True:
            try:
                if s_c[i:(i+2)]==['C','J']:
                    cost=cost+X
                if s_c[i:(i+2)]==['J','C']:
                    cost=cost+Y
            except:
                break
        cost_l.append(cost)
    print(min(cost_l))
