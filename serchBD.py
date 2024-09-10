import pandas as pd
df=pd.read_csv('data.csv')
print("Первые строки:")
print(df.head())  # Печатает первые 5 строк
print("\nПоследние строки:")
print(df.tail())  # Печатает последние 5 строк
print("\nКоличество строк и столбцов:", df.shape)
print("\nТип данных каждого поля:")
print(df.dtypes)
print("\nКоличество значений в каждом столбце:")
print(df.count())
del df['Id']
del df['DistrictId']
df = df.rename(columns={'Rooms':'Комнаты'})
df = df.rename(columns={'Square':'Площадь'})
df = df.rename(columns={'LifeSquare':'Жилая площадь'})
df = df.rename(columns={'KitchenSquare':'Площадь кухни'})
df = df.rename(columns={'Floor':'Этаж'})
df = df.rename(columns={'HouseYear':'Год постройки'})
df = df.rename(columns={'Ecology_1':'Экология'})
df = df.rename(columns={'Social_1':'Населённость'})
df = df.rename(columns={'Healthcare_1':'Забота о здоровье'})
df = df.rename(columns={'Shops_1':'Магазины'})
df = df.rename(columns={'Price':'Цена'})
print("\nСтолбец с ценой:")
print(df['Цена'])
print("\nПервая строка по номеру:")
print(df.iloc[0])
print("\nДесятая строка по номеру:")
print(df.iloc[9])
print("\nПредпоследняя строка по номеру:")
print(df.iloc[-2])
last_ten_rows = df.tail(10).drop(columns=['Цена'])

# Склейка с оригинальным датасетом
df = pd.concat([df, last_ten_rows], ignore_index=True)

# Заполнение отсутствующих значений цены средним
if 'Цена' in df.columns:  # Проверяем, существует ли столбец 'Цена'
    df['Цена'] = df['Цена'].fillna(df['Цена'].mean())
else:
    print("Столбец 'Цена' отсутствует в DataFrame.")
last_five_columns = df.iloc[:, -5:]  # Выделить последние 5 колонок
mean_price = df['Цена'].mean()
last_five_columns = last_five_columns[last_five_columns['Цена'] >= mean_price]
avg_price_per_floor = df.groupby('Этаж').agg({'Цена': 'mean', 'Этаж': 'count'}).rename(columns={'Этаж': 'Количество квартир'})
print("\nСредняя цена и количество квартир на каждом этаже:")
print(avg_price_per_floor)
avg_price_per_floor.to_csv('avg_price_per_floor.csv', index=False)
avg_price_per_floor.to_excel('avg_price_per_floor.xlsx', index=False)

# Проверка чтения файлов
print("\nПроверка CSV:")
print(pd.read_csv('avg_price_per_floor.csv'))
print("\nПроверка XLSX:")
print(pd.read_excel('avg_price_per_floor.xlsx'))