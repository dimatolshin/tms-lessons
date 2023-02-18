from person import Person

my_friends = [Person("emenem", 45, "M"), Person("gyf", 40, "M"), Person("sakyra", 25, "F")]


def get_oldest_pearson():
    older = my_friends[0]
    for i in my_friends[1:]:
        if i.age > older.age:
            older = i
    older.print_person_info()


def filter_male_person():
    gender = list(filter(lambda x: x.gender == "M", my_friends))
    for j in gender:
        j.print_person_info()


a = list(filter(lambda x: "M" in my_friends, my_friends))

my_friends[0].print_person_info()
my_friends[1].print_person_info()
my_friends[2].print_person_info()
get_oldest_pearson()
filter_male_person()
