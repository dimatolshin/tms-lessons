#* Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре. Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.


user=list(map(str,input().split()))
def map_to_tuples(user):
     not_word=['a', 'e', 'i', 'o', 'u']
     agard=list(filter(lambda x: (x not in list(map(str.upper,not_word)) and x not in list(map(str.lower,not_word))),user))
     return agard
print(map_to_tuples(user))