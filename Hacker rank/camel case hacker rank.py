import string
alphabets=list(string.ascii_letters)
ip=input()
op=''
case_flag=False
for ch in ip:
    if alphabets.count(ch)==0:
        case_flag=True
        print(case_flag)
    else:
        if case_flag:
            op+=ch.upper()
            case_flag=False
        else:
            op+=ch.lower()
print(op)
