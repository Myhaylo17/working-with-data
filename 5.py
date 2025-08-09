import pandas as pd
from collections import Counter
import ast  # Безпечніше за eval

# Шлях до файлів
tracks_path = r"C:\Users\mycha\Desktop\УАД\БД\laba6\tracks.csv"
artists_path = r"C:\Users\mycha\Desktop\УАД\БД\laba6\artists.csv"

# Завантаження даних
df_tracks = pd.read_csv(tracks_path)
df_artists = pd.read_csv(artists_path)

# Перетворення release_date у datetime
df_tracks['release_date'] = pd.to_datetime(df_tracks['release_date'], errors='coerce')

# Визначення десятиліття
df_tracks['decade'] = (df_tracks['release_date'].dt.year // 10) * 10

# Виправлення списку id_artists (він виглядає як: "['artist_id']")
df_tracks['id_artists'] = df_tracks['id_artists'].str.strip("[]").str.replace("'", "")

# Об'єднуємо з artists за artist_id
merged = df_tracks.merge(df_artists[['id', 'genres']], left_on='id_artists', right_on='id', how='left')

# Забираємо лише десятиліття та жанри
merged = merged[['decade', 'genres']].dropna()

# Розділяємо жанри на списки (без eval)
merged['genres'] = merged['genres'].apply(ast.literal_eval)

# Групуємо по десятиліттях і рахуємо найчастіші жанри
top_genres_by_decade = {}
for decade, group in merged.groupby('decade'):
    genre_list = [genre for sublist in group['genres'] for genre in sublist]
    common_genres = Counter(genre_list).most_common(5)
    top_genres_by_decade[decade] = common_genres

# Виводимо результат
for decade in sorted(top_genres_by_decade.keys()):
    print(f"\n{int(decade)}-ті роки:")
    for genre, count in top_genres_by_decade[decade]:
        print(f" {genre}: {count}")
