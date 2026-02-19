import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Шаг 1

data = {
    'age': [25, 62, 45, 70, 28, 65, 50, 81, 40, 68],
    'diagnosis': ['Грипп', 'ОРВИ', 'Бронхит', 'Грипп', 'ОРВИ', 'Пневмония', 'Бронхит', 'Пневмония', 'Грипп', 'ОРВИ'],
    'doctor': ['Хаус', 'Ватсон', 'Айболит', 'Ватсон', 'Хаус', 'Хаус', 'Айболит', 'Ватсон', 'Хаус', 'Ватсон'],
    'temp': [38.5, 37.2, 37.8, 39.1, 37.5, 38.9, 37.4, 38.0, 38.8, 37.1],
    'outcome': ['Выздоровление', 'Выздоровление', 'Осложнение', 'Выздоровление', 'Выздоровление', 
                'Осложнение', 'Выздоровление', 'Осложнение', 'Выздоровление', 'Выздоровление']
}

df = pd.DataFrame(data)
print("Таблица успешно загружена! Первые 3 строки:")
print(df.head(3))

# Шаг 2

df['age'].plot(kind='hist', title='Распределение возраста', color='skyblue', edgecolor='black')
plt.show()

df['diagnosis'].value_counts().plot(kind='bar', title='Популярные диагнозы', color='lightgreen')
plt.xticks(rotation=0)
plt.show()

# Шаг 3

plt.plot(df.index, df['temp'], marker='o', color='red')
plt.title('Температура пациентов')
plt.xlabel('Номер пациента')
plt.ylabel('Градусы')
plt.grid(True)
plt.show()

avg_temp = df.groupby('outcome')['temp'].mean()
plt.bar(avg_temp.index, avg_temp.values, color=['green', 'orange'])
plt.title('Средняя температура по исходу лечения')
plt.show()

# Шаг 4

sns.boxplot(data=df, x='diagnosis', y='age')
plt.title('Возраст пациентов при разных диагнозах')
plt.show()

sns.countplot(data=df, x='doctor', hue='outcome')
plt.title('Успехи лечащих врачей')
plt.show()

# Шаг 5

fig = px.scatter(df, x='age', y='temp', color='diagnosis', title='Интерактивный график: Возраст и Температура')
fig.show()