# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.


user=list(map(str,input().lower().split()))
def map_to_tuples(user):
     not_word=['a', 'e', 'i', 'o', 'u']
     agard=list(filter(lambda x: x not in not_word,user))
     return agard
print(map_to_tuples(user))


