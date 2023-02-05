def user(l:int)->list:
    k=[]
    for i in range(1,l+1):
        k.append(int(i)**3)
    return k
print(user(4))

