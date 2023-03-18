# (*) Пользователь вводит число, выведите True если оно простое, иначе False.
number = int(input())
result = ""
if  number == 1 :
    print('False')
elif  number == 2 :
    print('True')
for i in range(2, number):
    if number % i == 0 :
        result: str = 'False'
        break
    else:
        result = 'True'

print(result)
