
def mod(a, m):
    return (a%m + m) % m
t_c=int(input())
alpha='abcdefghijklmnopqrstuvwxyz'
for t in range(1,(t_c+1)):
    (n,k)=[int(x) for x in input().split()]
    s=input()
    s_len=len(s)
    temp_result1=['']
    for it in range(0,(round(s_len/2)+(s_len%2))):
        temp_result2=temp_result1
        temp_result1=[]
        for ie in temp_result2:
            i=ie
            i+=' '
            a=''
            a=alpha[:k]
            temp_result1.extend(i.join(a).split().copy())
            temp_result1[-1]+=ie
#        print(f'a {a}')
    temp_result2=[j[::-1]+j[(s_len%2):] for j in temp_result1]
    temp_result2.append(s)
    temp_result2.sort()
    ans=mod(temp_result2.index(s),1000000000)
#    print(temp_result2)

    print(f'Case #{t}: {ans}')

        
        
