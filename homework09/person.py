import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print("Person:", self.full_name, self.gender, self.age, "years old")

    def get_birth_year(self):
        years_now = datetime.datetime.now()
        return years_now.year - self.age


if __name__ == '__main__':
    my_person = Person("Dima", 24, "M")
    my_person.print_person_info()
    print(my_person.age)
    print(my_person.full_name)
    print(my_person.gender)
    print(my_person.get_birth_year())
