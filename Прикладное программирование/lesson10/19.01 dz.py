import pandas as pd
import io

def print_section(title):
    print(f"\n {title.upper()}")
    print("=" * 40)

# ШАГ 2: База данных

hospital_data = {
    'episode_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'patient_name': ['Иванов И.И.', 'Петров П.П.', 'Сидорова А.А.', 'Кузнецов К.К.', 'Смирнова Е.Е.', 
                     'Попов Д.Д.', 'Васильев В.В.', 'Макарова М.М.', 'Лебедев Л.Л.', 'Морозова Н.Н.'],
    'age': [35, 62, 45, 70, 28, 65, 50, 81, 40, 68],
    'diagnosis': ['Грипп', 'Гипертония', 'Гастрит', 'Диабет', 'ОРВИ', 
                  'Гипертония', 'Бронхит', 'Артрит', 'Грипп', 'Диабет'],
    'doctor': ['Др. Хаус', 'Др. Ватсон', 'Др. Айболит', 'Др. Ватсон', 'Др. Хаус', 
               'Др. Стрэндж', 'Др. Айболит', 'Др. Стрэндж', 'Др. Хаус', 'Др. Ватсон'],
    'outcome': ['Выздоровление', 'Стабильно', 'Лечение', 'Стабильно', 'Выздоровление', 
                'Ухудшение', 'Выздоровление', 'Стабильно', 'Выздоровление', 'Лечение']
}

df = pd.DataFrame(hospital_data)

# ШАГ 3

print_section("Первые пациенты в списке")
print(df.head())

print_section("Размер базы данных")
rows, cols = df.shape
print(f"Записей: {rows}, Колонок: {cols}")

print_section("Проверка на ошибки")
print(df.isna().sum()) 

# ШАГ 4

df = df.set_index('episode_id')

print_section("Вид таблицы где 'индекс = ID случая'")
print(df.head(3))

df = df.reset_index().set_index('episode_id')

# ШАГ 5

print_section("Поиск: Сидорова А.А.")
print(df.query("patient_name == 'Сидорова А.А.'"))

print_section("Диагноз: Гипертония")
print(df.query("diagnosis == 'Гипертония'"))

print_section("Группа риска: Старше 60 лет")
print(df.query("age > 60"))

print_section("Точечный поиск")
print("По ID 102:")
print(df.loc[102]) 
print("\n По номеру строки 1:")
print(df.iloc[1])

# ШАГ 6

new_patients_csv = """episode_id,patient_name,age,diagnosis,doctor,outcome
201,Зайцев З.З.,33,Перелом,Др. Стрэндж,Выздоровление
202,Волков В.В.,44,Ушиб,Др. Хаус,Выздоровление
203,Лисицына Л.Л.,25,Гастрит,Др. Айболит,Лечение
"""

df_new = pd.read_csv(io.StringIO(new_patients_csv)).set_index('episode_id')

print_section("Загружено из CSV")
print(df_new)