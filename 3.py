import pandas as pd
# Зчитуємо дані
df = pd.read_csv(r"C:\Users\mycha\Desktop\УАД\БД\laba6\tracks.csv")
# Знаходимо поріг 90-го перцентиля за популярністю
popularity_threshold = df['popularity'].quantile(0.9)
# Відбираємо топ-10% пісень
top_songs = df[df['popularity'] >= popularity_threshold]
# Список звукових фіч
audio_features = [
 'danceability', 'energy', 'valence', 'tempo',
 'acousticness', 'instrumentalness', 'speechiness',
 'liveness', 'loudness'
]
# Обчислюємо середнє значення кожної фічі для топ-пісень
top_audio_means = top_songs[audio_features].mean().sort_values(ascending=False)
# Виводимо результат
print("Середні значення звукових фіч у 10% найпопулярніших треків:")
print(top_audio_means)