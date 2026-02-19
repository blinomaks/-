import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

# Шаг 1

np.random.seed(42)
data = {
    'patient_id': range(1001, 1101),
    'age': np.random.randint(18, 85, 100),
    'gender': np.random.choice(['М', 'Ж'], 100),
    'temperature': np.round(np.random.uniform(36.0, 39.5, 100), 1),
    'diagnosis': np.random.choice(['Грипп', 'ОРВИ', 'Бронхит', 'Пневмония'], 100),
    'days_in_hospital': np.random.randint(3, 15, 100)
}

df = pd.DataFrame(data)

df.loc[[10, 45, 88], 'days_in_hospital'] = np.nan 

df['outcome'] = np.where((df['diagnosis'] == 'Пневмония') | (df['temperature'] > 38.5), 'Осложнение', 'Выздоровление')

print(df.head())

# Шаг 2

print("Количество строк и столбцов:")
print(df.shape)

print("\nНаличие пропусков:")
print(df.isna().sum())

print("\nБазовые статистики числовых признаков:")
print(df.describe())

# Шаг 3

median_days = df['days_in_hospital'].median()
df['days_in_hospital'] = df['days_in_hospital'].fillna(median_days)

X_raw = df[['age', 'gender', 'temperature', 'diagnosis']]
y_raw = df['outcome']

X = pd.get_dummies(X_raw, columns=['gender', 'diagnosis'])
y = y_raw.map({'Выздоровление': 1, 'Осложнение': 0})

print("Данные готовы к обучению (первые 3 строки):")
print(X.head(3))

# Шаг 4 и 5

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train) 

predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)
prec = precision_score(y_test, predictions)
rec = recall_score(y_test, predictions)

print(f"Accuracy (общая точность): {acc:.2f}")
print(f"Precision (точность): {prec:.2f}")
print(f"Recall (полнота): {rec:.2f}")

# Шаг 6

results_df = pd.DataFrame({
    'Реальный_Исход': y_test.map({1: 'Выздоровление', 0: 'Осложнение'}).values,
    'Предсказание': pd.Series(predictions).map({1: 'Выздоровление', 0: 'Осложнение'}).values
})
print(results_df.head())


print("\n--- Шаг 7. Экспорт и сохранение данных ---")
results_df.to_csv('predictions_report.csv', index=False)

joblib.dump(model, 'medical_model.pkl')
print("Файлы predictions_report.csv и medical_model.pkl успешно сохранены!")