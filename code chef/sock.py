# cook your dish here
i_p=input().split()
result=False
comp=i_p.pop()
print(comp,i_p)
try:
    i_p.index(comp)
    print(i_p.index(comp))
    result=result or True
except:
    pass
comp=i_p.pop()
try:
    i_p.index(comp)
    print(i_p.index(comp))
    result=result or True
except:
    pass
if result:
    print('yes')
else:
    print('no')
