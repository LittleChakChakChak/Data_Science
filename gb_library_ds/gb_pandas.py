import pandas as pd
import numpy as np
import pickle

def task_1():
    # создание дата фреймов
    authors = pd.DataFrame([[1, 'Тургенев'], [2, 'Чехов'], [3, 'Островский']], columns=['author_id', 'author_name'])

    array_book = [[1, 'Отцы и дети', 450],
                  [1, 'Рудин', 300],
                  [1, 'Дворянское гнездо', 350],
                  [2, 'Толстый и тонкий', 500],
                  [2, 'Дама с собачкой', 450],
                  [3, 'Гроза', 370],
                  [3, 'Таланты и поклонники', 290]]

    book = pd.DataFrame(array_book, columns=['author_id', 'book_title', 'price'])

    print(authors, '\n', book)

    return authors, book


def task_2(df1, df2):
    # соединение дата фреймов
    authors_price = df1.merge(df2)

    print(authors_price)

    return authors_price

def task_3(df):
    # 5 самых дорогих позиций
    df_sort = df.sort_values(by='price', ascending=False)

    top5 = df_sort.head()
    print(top5)

    return top5


def task_4(df, list_name):
    # создание пустого дата фрема
    authors_stat = pd.DataFrame(columns=['author_name', 'min_price', 'max_price', 'mean_price'])

    for name in list_name:
        filter_name = df.query('author_name == @name')

        # заполнение
        authors_stat.loc[len(authors_stat.index)] = [name,
                                                     filter_name['price'].min(),
                                                     filter_name['price'].max(),
                                                     filter_name['price'].mean()]

    print(authors_stat)
    return authors_stat


def task_5(df, array):
    # добавляем столбец
    df['cover'] = array
    # создание нового дата фрейма по условиям
    book_info = pd.pivot_table(data=df, values=['price'], index=['author_name'], columns=['cover'], fill_value=0, aggfunc=np.sum)
    print(f'------- До сохранения -------\n {book_info}')
    pickle.dump(book_info, open("book_info.pkl", "wb"))

    # читаем файл
    book_info2 = pickle.load(open("book_info.pkl", "rb"))
    print(f'------- После сохранения -------\n {book_info2}')

authors, book = task_1()
authors_price = task_2(authors, book)
top5 = task_3(authors_price)
authors_stat = task_4(authors_price, ['Тургенев', 'Чехов', 'Островский'])
task_5(authors_price, ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'])