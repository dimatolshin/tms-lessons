def user(year:int)->bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0
print(user(2104))





