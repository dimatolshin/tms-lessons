from student import Student

students = [Student("Marina", 5), Student("Nikita", 10), Student("Diana", 8), Student("Dima", 9)]


def calc_sum_scholarship():
    summ = 0
    for x in students:
        summ += x.get_scholarship()
    return summ


def get_excellent_student_count():
    excellent = 0
    for i in students:
        if i.is_excellent():
            excellent += 1
    return excellent


print(calc_sum_scholarship(), "Рублей")
print(get_excellent_student_count())
