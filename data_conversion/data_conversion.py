import pandas as pd


def skip_percentage(column):
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
    data[column] = abs(data[column])
    # проверка
    print(data[column].head(15))


data = pd.read_csv('data.csv')

# просмотр значений в файле data.csv
# print(data.value_counts())

# search_for_passes(data)
# replacing_passes('days_employed')
# replacing_passes('total_income')
fixing_artifacts('days_employed')
# print(data['days_employed'])


