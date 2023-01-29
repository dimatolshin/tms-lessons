#Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
month=str(input().lower())
day=int(input())
choice={"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
key=choice[month]
if day<=key:
    print(True)
else:
    day>key
    print(False)

