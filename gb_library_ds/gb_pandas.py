import pandas as pd

def task_1():
    # создание дата фреймов
    authors = pd.DataFrame([[1, 'Тургенев'], [2, 'Чехов'], [3, 'Островский']], columns=['author_id', 'author_name'])

    array_book = [[1, 'Отцы и дети',450],
                  [1, 'Рудин',300],
                  [1, 'Дворянское гнездо',350],
                  [2, 'Толстый и тонкий',500],
                  [2, 'Дама с собачкой',450],
                  [3, 'Гроза',370],
                  [3, 'Таланты и поклонники',290]]

    book = pd.DataFrame(array_book, columns=['author_id', 'book_title', 'price'])

    print(authors)
    print(book)

task_1()