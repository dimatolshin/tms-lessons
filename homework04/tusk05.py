user = int(input())
summ = 0
while user!=0:
    ostatok = user % 10
    summ += ostatok
    user = user//10
print(summ)
