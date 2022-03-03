from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# получаем данные по Бостовским домам
x, y = load_boston(return_X_y=True)

print('X:')
print(x[:3])
print()
print('Y:')
print(y[:3])

# разделение данных на обучающую и тестовую

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

# стандартерезуем данные

scaler = StandardScaler().fit(x_train)
standardized_X = scaler.transform(x_train)

print('До стандартизации:')
print(x_train[:3])
print()
print('После стандартизации:')
print(standardized_X[:3])

# нормализуем

scaler = Normalizer().fit(x_test)
normalized_X = scaler.transform(x_test)

print('До нормализации:')
print(x_test[:3])
print()
print('После нормализации:')
print(normalized_X[:3])

data = [[178, 500000, 58], [130, 5000, 110], [190, 100000000, 90]] # запись о людях (рост, зарплата, вес) другой пример

scaler = Normalizer().fit(data)
normalized_data = scaler.transform(data)

print('До нормализации:')
print(data[:3])
print()
print('После нормализации:')
print(normalized_data[:3]) # теперь нет гигантской разницы в признаках

# приведение к бинарному ввиду

X = 10 * np.random.random((5, 5)) - 5

binarizer = Binarizer(threshold=0.0).fit(X) # в данном случае порог 0.0
binary_X = binarizer.transform(X)

print('До бинаризации:')
print(X[:5])
print()
print('После бинаризации:')
print(binary_X[:5])

absenteeism_number_student = np.array([[3, 1, 5, 0, 2, 5, 9, 888]]) # количество прогулов у студентов

binarizer = Binarizer(threshold=3.0).fit(absenteeism_number_student) # порог прогулов 3
binary_absenteeism_number_student = binarizer.transform(absenteeism_number_student)

print()
print('Прогульщики в бинарном ввиде')
print(binary_absenteeism_number_student)

# Кодирование признаков

country = np.array(['rus', 'usa', 'ua', 'usa', 'rus']) # наш признак - строкове сокращение страны

enc = LabelEncoder()
print()
print('Страны до изменения:')
print(country)
print('Страны после изменений:')
print(enc.fit_transform(country))


# Обучение моделей

    # с учителем
"""
# данные
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]]) # обучающая выборка
y = np.dot(X, np.array([1, 2])) + 3  # тестовая выборка

# создаём объект модели, настраиваем парметры
lr = LinearRegression(normalize=True)

lr.fit(X, y)

# обучаем модель, передав обучающую выборку X и тестовую выборку Y
lr = LinearRegression().fit(X, y)
"""
    # без учителя

X = np.array([[1, 2], [1, 4], [1, 0],
             [10, 2], [10, 4], [10, 0]]) # обучающая выборка, тестовой нет

kmeans = KMeans(n_clusters=2, random_state=0) # создаём объект модели, настриваем параметры
kmeans = kmeans.fit(X) # обучаем модель

# тестовые или новые данные для которых мы хотим получить предсказание
test = np.array([[5, 1], [0, 3], [2, 1], [11, 1], [9, 3], [9, 1]])

y = kmeans.predict(test)  # предсказываем
print('Predict: ', y)

# на этом, пока что, изучение про модели остановилось