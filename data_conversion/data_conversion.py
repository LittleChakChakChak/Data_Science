import pandas as pd

DACH = '-'


def skip_percentage(column):
    # получение процента пропусков по колонке
    percentage = (column[1] / (column[1] + column[0])) * 100
    return f'{column.name}, values: Nan = {int(percentage)}%'


def search_for_passes(data):
    # поиск уникального значения столбцов
    print(data.isnull().value_counts())
    nan_days_employed = data['days_employed'].isnull().value_counts()
    nan_total_income = data['total_income'].isnull().value_counts()
    # поиск % days_employed
    print(skip_percentage(nan_days_employed))
    # поиск % total_income
    print(skip_percentage(nan_total_income))


def replacing_passes(column):
    # пропущенные значения будут заполнены медианой по колонке
    median_value = data[column].median()
    data[column] = data[column].fillna(median_value)
    # проверка
    print(data[column].isnull().value_counts())


def fixing_artifacts(column):
    # исправление артифактов (избавление от отрицательных дней)
    data[column] = abs(data[column])
    # проверка
    print(data[column].head(15))


def type_replacement(column, new_type, data):
    # изменение типа в колонке
    try:
        return data.astype({column: new_type})
    except:
        print('Ошибка при изменение типа')


def duplicates_work(column):
    # изменение регистра колонки

    # до изменения
    print(data[column].duplicated().value_counts())

    data[column] = data[column].str.lower()
    # проверка (после изменения)
    print(data[column].duplicated().value_counts())


data = pd.read_csv('data.csv')

# просмотр значений в файле data.csv
# print(data.value_counts())

print('Поиск пропусков' + DACH * 50)
search_for_passes(data)

print('Замена пропусков средним значением' + DACH * 50)
replacing_passes('days_employed')
replacing_passes('total_income')

print('Очистка от артефакта' + DACH * 50)
fixing_artifacts('days_employed')

print('Изменени типа столбца "ежемесячный доход"' + DACH * 50)
data = type_replacement('total_income', 'int64', data)
print(f"Тип колонки total_income = {data['total_income'].dtypes}")


print('Избавление от дублей"' + DACH * 50)
duplicates_work('education')
print(data['education'].head(15))

print('Проверка остальных столбцов с строками на дубли"' + DACH * 50)
duplicates_work('family_status')
duplicates_work('gender')
duplicates_work('income_type')
duplicates_work('purpose')

