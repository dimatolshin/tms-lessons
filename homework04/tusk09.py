s=(list(map(str,input().split())))
def user(s):
    _len=len(s[0])
    summ=s[0]
    for i in range(1,len(s)):
        if len(s[i])>_len:
            _len=len(s[i])
            summ=s[i]
    return summ
print(user(s))




