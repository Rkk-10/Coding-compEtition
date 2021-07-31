T=int(input())
for c in range(0,T):
    N=int(input())
    #cal=[]
    cal_a=[]
    cal_b=[]
    cal_c=[]
    cal_d=[]
    while N:
        if N>0:
            cal_a.append(N)
            N-=1
        if N>0:
            cal_b.append(N)
            N-=1
        if N>0:
            cal_c.append(N)
            N-=1
        if N>0:
            cal_d.append(N)
            N-=1
    print(cal_a,cal_b,cal_c,cal_d)
    #cal.append(cal_a.copy())
    #cal.append(cal_b.copy())
    #cal.append(cal_c.copy())
    #cal.append(cal_d.copy())
    #print(cal)


"""    l_a=len(cal_a)
    l_b=len(cal_b)
    l_c=len(cal_c)
    l_d=len(cal_d)
    result=(l_a-1)*8
    if l_a>l_d:
        result+=5
        if l_b>l_d:
            result+=3
            if l_c>l_d:
                result+=4
            else:
                result+=2
        else:
            result+=2
    else:
        result+=12
"""
    l_a=len(cal_a)
    l_b=len(cal_b)
    l_c=len(cal_c)
    l_d=len(cal_d)
    result=(l_a-1)*44
"""
    if l_a>l_d:
        result+=18
        if l_b>l_d:
            result+=15
            if l_c>l_d:
                result+=18
            else:
                result+=11
        else:
            result+=6
    else:
        result+=60
    print(result)
"""
    if l_a==l_b and l_b==l_c and l_c==l_d:
        result+=60
    elif l_a==l_b and l_b==l_c:
        result+=55
    elif l_a==l_b:
        result+=44
    else:
        result+=32
    print(result)
