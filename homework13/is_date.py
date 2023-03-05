import re


def nomber(user):
    return re.fullmatch(r'[0-3]\d[-][0-1]\d[-][1-2]\d{3}', user) is not None


def is_float_number(user):
    return re.fullmatch(r'\d+[.]\d+', user) is not None


class WordIterable:
    def __init__(self, stroka):
        self.stroka = stroka.split()
        self.count = 0

    def __iter__(self):
        self.user = self.stroka
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.user):
            raise StopIteration
        return self.user[self.count - 1]


class WordIterable_2:
    def __init__(self, stroka):
        self.stroka = re.findall(r'(?i)([а-я]+)', stroka)
        self.count = 0

    def __iter__(self):
        self.user = self.stroka
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.user):
            raise StopIteration
        return self.user[self.count - 1]


def generate_words(stroka):
    for i in stroka.split():
        yield i


def generate_words_2(stroka):
    stroka = re.findall(r'(?i)([а-я]+)', stroka)
    for i in stroka:
        yield i


if __name__ == '__main__':
    assert nomber('21-02-1999')
    assert not nomber('221-03-1999')
    assert not nomber('21-033-1999')
    assert not nomber('21-03-21111')
    assert not nomber('2f-21-1111')
    assert not nomber('21-f3-11111')
    assert not nomber('21-21-dfs2')
    assert not nomber('21-21-1999')
    assert not nomber('34-15-3455')
    assert is_float_number("21.2")
    assert is_float_number("1111111.11111111")
    assert is_float_number("01111.234124")
    assert not is_float_number("fd.2")
    assert not is_float_number("2.1.2")
    assert not is_float_number("21.g1")

    for i in WordIterable('мама мыла раму'):
        print(i)

    for i in WordIterable_2('мама! мыла, раму?'):
        print(i)

    for i in generate_words('мама мыла раму'):
        print(i)

    for i in generate_words_2('мама! мыла, раму?'):
        print(i)

    assert ['мама', 'мыла', 'раму'] == [i for i in WordIterable('мама мыла раму')]
    assert ['мама', 'мыла', 'раму'] == [i for i in WordIterable_2('мама! мыла, раму?')]
    assert ['мама', 'мыла', 'раму'] == [i for i in generate_words('мама мыла раму')]
    assert ['мама', 'мыла', 'раму'] == [i for i in generate_words_2('мама! мыла, раму?')]