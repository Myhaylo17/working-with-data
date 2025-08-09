import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Зчитуємо дані
df = pd.read_csv(r"C:\Users\mycha\Desktop\УАД\БД\laba6\tracks.csv")
# Список звукових фіч для аналізу
audio_features = [
 'danceability', 'energy', 'valence', 'tempo',
 'acousticness', 'instrumentalness', 'speechiness',
 'liveness', 'loudness'
]
# Розраховуємо кореляцію між популярністю і звуковими фічами
correlation = df[audio_features + ['popularity']].corr()
# Виводимо кореляційну матрицю
print("Кореляція між популярністю і звуковими функціями:")
print(correlation['popularity'])
# Побудова теплової карти для візуалізації
plt.figure(figsize=(10, 6))
sns.heatmap(correlation[['popularity']], annot=True, cmap='coolwarm', vmin=-1,
vmax=1)
plt.title('Кореляція між популярністю та з')