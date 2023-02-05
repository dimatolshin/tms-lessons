def user(*args):
    k=[]
    for i in args:
        k.append(int(i)**2)
    return k
print(user(1,2,3,4))
