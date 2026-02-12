import pandas as pd
import numpy as np

# Шаг №1

data = {
    'episode_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
    'patient_name': ['Иванов И.И.', 'Петров П.П.', 'Сидорова А.А.', 'Кузнецов К.К.', 'Смирнова Е.Е.', 
                     'Попов Д.Д.', 'Васильев В.В.', 'Макарова М.М.', 'Лебедев Л.Л.', 'Морозова Н.Н.', 'Неизвестный Н.'],
    'age': [35, 62, 45, 70, 28, 65, 50, 81, 40, 68, np.nan],
    'diagnosis': ['Грипп', 'Гипертония', 'Гастрит', 'Диабет', 'ОРВИ', 
                  'Гипертония', 'Бронхит', 'Артрит', 'Грипп', 'Диабет', 'Ушиб'],
    'doctor': ['Др. Хаус', 'Др. Ватсон', 'Др. Айболит', 'Др. Ватсон', 'Др. Хаус', 
               'Др. Стрэндж', 'Др. Айболит', 'Др. Стрэндж', 'Др. Хаус', 'Др. Ватсон', 'Др. Хаус'],
    'outcome': ['Выздоровление', 'Стабильно', 'Лечение', 'Стабильно', 'Выздоровление', 
                'Ухудшение', 'Выздоровление', 'Стабильно', 'Выздоровление', 'Лечение', 'Выздоровление']
}

df = pd.DataFrame(data)

print("--- Исходная таблица ---")
print(df.head())

# Шаг №2

print("\n--- Старше 60 лет ---")
f1 = df[df['age'] > 60]
print(f1)

print("\n--- Младше 40 с диагнозом 'Грипп' ---")
f2 = df[(df['age'] < 40) & (df['diagnosis'] == "Грипп")]
print(f2)

print("\n--- От 30 до 70 лет ---")
f3 = df[(df['age'] >= 30) & (df['age'] <= 70)]
print(f3)

# Шаг №3

print("\n--- Люди с ухудшением здоровья ---")
print(df[df['outcome'] == 'Ухудшение'])

print("\n--- Возраст не указан ---")
print(df[df['age'].isna()])

# Шаг №4

print("\n--- Сортировка по возрасту (возрастание) ---")
s1 = df.sort_values(by='age')
print(s1.head())

print("\n--- Сортировка по возрасту (убывание) ---")
s2 = df.sort_values(by='age', ascending=False)
print(s2.head())

print("\n--- Сортировка по диагнозу и возрасту ---")
s3 = df.sort_values(by=['diagnosis', 'age'])
print(s3)

# Шаг №5

print("\n--- Группировка по диагнозу ---")
group_res = df.groupby('diagnosis').agg({
    'episode_id': 'count',
    'age': 'mean'
})
print(group_res)

# Шаг №6

df['senior'] = df['age'] > 60
print("\n--- Добавили столбец senior ---")
print(df.head(3))

df = df.drop(columns=['senior'])
print("--- Удалили столбец ---")

# Шаг №7 и №8

print("\n--- Типы данных до изменений ---")
print(df.dtypes)

df['episode_id'] = df['episode_id'].astype(str)
df = df.rename(columns={'episode_id': 'Case_ID', 'patient_name': 'Patient'})

print("\n--- Типы данных после изменений ---")
print(df.dtypes)
print("\n--- Финальный вид таблицы ---")
print(df.head())