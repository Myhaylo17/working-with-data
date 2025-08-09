import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Зчитуємо дані
df = pd.read_csv(r"C:\Users\mycha\Desktop\УАД\БД\laba6\tracks.csv")
# Знаходимо пісню з найвищою популярністю
most_popular_song = df.loc[df['popularity'].idxmax()]
# Список звукових фіч
audio_features = [
 'danceability', 'energy', 'valence', 'tempo',
 'acousticness', 'instrumentalness', 'speechiness',
 'liveness', 'loudness'
]
# Отримуємо характеристики найпопулярнішої пісні
most_popular_values = most_popular_song[audio_features]
# Розраховуємо середнє значення для кожної фічі по всіх піснях
average_values = df[audio_features].mean()
# Побудова графіка для порівняння характеристик найпопулярнішої пісні та середніх значень
plt.figure(figsize=(10, 6))
# Графік для найпопулярнішої пісні
sns.barplot(x=most_popular_values.index, y=most_popular_values.values,
color='b', label='Найпопулярніша пісня')
# Графік для середніх значень
sns.barplot(x=average_values.index, y=average_values.values, color='r',
label='Середні значення')
# Додавання підписів та легенди
plt.title('Порівняння звукових функцій найпопулярнішої пісні та середніхзначень')
plt.xlabel('Звукові характеристики')
plt.ylabel('Значення')
plt.xticks(rotation=45)
plt.legend()
# Показуємо