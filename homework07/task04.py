#Пользователь вводит произвольное количество слов через пробел. Затем (на следующей строке) вводит один символ (разделитель).
#Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить,
# и возвращает строку, в которой все слова из списка соединены через символ разделитель.

#                                1 method
# user=list(map(str,input().split()))
# def my_join(user):
#     s = "@"
#     return s.join(user)
# print(my_join(user))


#                                 2 method

# from functools import reduce
# user = input().split()
# s = input()
# def my_join():
#      return [(i + s) for i in user]
# agard=reduce(lambda x,y: x+y , my_join())
# agard=agard[:-1]
# print(agard)