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


def new_dataframe(column_id, column):
    # создание отдельных дата фреймов
    df = pd.DataFrame({column_id: data[column_id], column: data[column]})
    return df


def drop_column(column):
    # удаление колонок
    data.drop(columns=[column], axis=1, inplace=True)
    return f'Колонка {column} удалена'


def income_categories(value):
    # категории по прибыли
    if value >= 1000001:
        return 'A'
    elif 200001 <= value <= 1000000:
        return 'B'
    elif 50001 <= value <= 200000:
        return 'C'
    elif 30001 <= value <= 50000:
        return 'D'
    elif 0 < value <= 30000:
        return 'E'
    else:
        print('Нет подходящей категории для ', value)


def purpose_categories(value):
    # категории по назначению
    if 'авто' in value:
        return 'операции с автомобилем'
    elif 'недвиж' or 'жиль' in value:
        return 'операции с недвижимостью'
    elif 'свадьб' in value:
        return 'проведение свадьбы'
    elif 'образов' in value:
        return 'получение образования'
    else:
        print('Нет подходящей категории для ', value)


def viewing_dependencies(column_0, column_1='debt'):
    return data[[column_0, column_1]].value_counts()


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

print('Создание отдельных dataframe"' + DACH * 50)
df_education = new_dataframe('education_id', 'education')
print(df_education.head(15))
print(drop_column('education'))

df_family_status = new_dataframe('family_status_id', 'family_status')
print(df_family_status.head(15))
print(drop_column('family_status'))

print(data.dtypes)

print('Категории по приболи' + DACH * 50)
data['total_income_category'] = data['total_income'].apply(income_categories)
print(data[['total_income', 'total_income_category']].head(15))

print('Категории по назначению' + DACH * 50)
data['purpose_category'] = data['purpose'].apply(purpose_categories)
print(data[['purpose', 'purpose_category']].head(15))

# сохранение дата фрейма
# data.to_csv('new_data.csv')

# Есть ли зависимость между количеством детей и возвратом кредита в срок?
print(viewing_dependencies('children'))

# Есть ли зависимость между семейным положением и возвратом кредита в срок?
print(viewing_dependencies('family_status_id'))
print(df_family_status.value_counts())

# Есть ли зависимость между уровнем дохода и возвратом кредита в срок?
print(viewing_dependencies('total_income_category'))

# Как разные цели кредита влияют на его возврат в срок?
print(viewing_dependencies('purpose_category'))
