def get_most_frequent_word():
    user = list(map(str, input().split()))
    word = ''
    for i in user:
        if user.count(i) > user.count(word):
            word = i
    return word


print(get_most_frequent_word())
