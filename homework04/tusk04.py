import random
a = random.randint(0, 100)
while True:
    user = int(input())
    if user == a:
        print("Поздравляю вы угадали число", a)
        break
    if user<a:
        print("Вы не удагадали, ваше число меньше  загаданого")
    if user>a:
        print("Вы не удагадали, ваше число больше загаданого")

