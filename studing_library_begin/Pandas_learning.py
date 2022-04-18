import pandas as pd

auto = pd.read_csv('Automobile_data.csv')
print(auto)
print('-' * 40)
auto_modified = auto.set_index('make')
print(auto_modified)
print('-' * 40)

print(auto.columns.tolist())
print(auto['make'].tolist())

# Вывод статистических сведений о датафрейме
print(auto.describe())
print('-' * 40)

print(len(auto['make'].unique()))
print(auto['make'].unique())
print('-' * 40)

price_auto = auto[['make', 'price']]
print(price_auto)
print('-' * 40)

print(auto[auto['make'].isin(['audi', 'bmw'])])
print('-' * 40)