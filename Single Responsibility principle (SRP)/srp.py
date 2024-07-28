"""Принцип единственной ответсвенности
    класс или функция должны выполнять ровно одно логическое действие"""

""" Вариант 1
    Как не надо делать"""
class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def save_in_db(self):
        # Сохраняем юзера в БД
        pass


"""Как надо делать"""
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class UserModelDB:
    def get_username_from_db(self, user_id):
        pass

    def save_in_db(self, user):
        pass


"""Вариант 2
    Как не надо делать"""
def percentage_of_word(search, file):
    search = search.lower()
    content = open(file, 'r').read()
    words = content.split()
    number_of_words = len(words)
    occurrences = 0
    for word in words:
        if word.lower() == search:
            occurrences += 1
        return occurrences / number_of_words


"""Как надо делать"""
def read_localfile(file):
    return open(file, 'r').read()


def number_of_words(content):
    return len(content.split())


def count_word_occurrences(word, content):
    counter = 0
    for e in content.split():
        if word.lower() in e.lower():
            counter += 1
        return counter


def percentage_of_word(word, content):
    total_words = number_of_words(content)
    word_occurrences = count_word_occurrences(word, content)
    return word_occurrences / total_words


def percentage_of_words_in_localfile(word, file):
    content = read_localfile(file)
    return percentage_of_word(word, content)
