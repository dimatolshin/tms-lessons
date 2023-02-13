# Напишите функцию-декоратор my_decorator, в которую можно обернуть функцию, которая принимает один входной параметр.
# Ваш декоратор должен будет выводить в консоль входной параметр оборачиваемой функции,
# запускать функцию, а затем выводить результат этой функции.


def my_decorator(funk):
    def second_operation(*args,**kwargs):
        print("Функция получила на вход значение",n)
        result=funk(*args,**kwargs)
        print("результат функции=",result)
        return result
    return second_operation






@my_decorator
def my_func(x):
   return x ** 2

n=int(input("введите число "))
y = my_func(n)
print(f'y = {y}')