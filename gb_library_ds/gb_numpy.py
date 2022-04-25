import numpy as np

def task_1(array):
    # среднее значение по стобцам
    return np.mean(array, axis=0)


def task_2(array, array_mean):
    # a_centered = a - mean_a
    return array - array_mean

def task_3(array):
    # ищем скалярное произведение столбов массива, после чего делим на число наблюдений
    column_1 = array[:, 0]
    column_2 = array[:, 1]
    sp = np.dot(column_1, column_2)
    return sp / (len(column_1) - 1)

def task_4(array):
    # проверка ковариации
    column_1 = array[:, 0]
    column_2 = array[:, 1]
    a_transponir = np.array([column_1,
                            column_2])
    chek_covariance = np.cov(a_transponir)
    return chek_covariance[0][1]


a = np.array([[1, 6],
            [2, 8],
            [3, 11],
            [3, 10],
            [1, 7]])

print('-' * 50)
mean_a = task_1(a)
print(f'Среднии значения по столбцам: {mean_a}')

print('-' * 50)
a_centered = task_2(a, mean_a)
print(f'Вычитание массивов: \n {a_centered}')

print('-' * 50)
a_centered_sp = task_3(a_centered)
print(f'Ковариация: {a_centered_sp}')

print('-' * 50)
a_covariance = task_4(a)
print(f'Проверка ковариация: {a_covariance}')