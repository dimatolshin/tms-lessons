class Student():
    def __init__(self, full_name, average_mark):
        self.full_name = full_name
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark < 6:
            return 60
        elif self.average_mark >= 6 and self.average_mark < 8:
            return 80
        elif self.average_mark >= 8:
            return 100

    def is_excellent(self):
        return self.average_mark >= 9


if __name__ == '__main__':
    user = Student('Dima', 7)
    print(user.full_name)
    print(user.average_mark)
    print(user.get_scholarship(), "Рублей")
    print(user.is_excellent())
