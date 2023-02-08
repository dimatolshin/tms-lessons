def user(s):
     return s*3

def summ(x:int,y:int):
    return x+y


def choise(a:int,b:int)->bool:
     return a<b


def user_1(a,b)->int:
     if a<b:
         return -1
     if a>b:
         return 1
     elif a==b:
         return 0


def gost(args):
     k=[]
     for i in args:
         if int(i)<=0:
             continue
         else:
             k.append(int(i))
     return k


name=int(input("Выберите номер задачи "))
if name==1:
    print(user("helo_world "))
elif name==2:
    x=int(input("Введите 1 число "))
    y=int(input("Введите 2 число "))
    print("Сумма чисел равна =",summ(x,y))
elif name==3:
    a = int(input("Введите 1 число "))
    b = int(input("Введите 2 число "))
    print("второе число больше первого?",choise(a,b))
elif name==4:
    a = int(input("Введите 1 число "))
    b = int(input("Введите 2 число "))
    print("вывод", user_1(a, b))
elif name==5:
    args = list(map(int,input("Введите числа через пробел ").split()))
    print("Ваш новый список без отрицательных чисел выглядит вот так ",gost(args))
else:
    print("Номера такой задачи нет ")













