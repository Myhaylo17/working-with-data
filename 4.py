import pandas as pd
import matplotlib.pyplot as plt

# Зчитуємо дані
df = pd.read_csv(r"C:\Users\mycha\Desktop\УАД\БД\laba6\tracks.csv")
# Перетворюємо стовпець 'release_date' у формат datetime
# Якщо дата містить тільки рік, перетворюємо її в дату початку року (1 січня)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce',
format='%Y', utc=False)
# Якщо є NaT (невалідні дати), заповнюємо їх значеннями на 1 січня цього року
df['release_date'].fillna(pd.to_datetime(df['release_date'], format='%Y',
errors='coerce'), inplace=True)
# Створюємо стовпець для десятиліття
df['decade'] = (df['release_date'].dt.year // 10) * 10
# Вибираємо тільки потрібні функції: темп, валентність, гучність
features = ['tempo', 'valence', 'loudness']
# Групуємо за десятиліттями та обчислюємо середні значення
decade_avg = df.groupby('decade')[features].mean()
# Побудова графіків для кожної функції
plt.figure(figsize=(14, 8))
# Темп
plt.subplot(3, 1, 1)
plt.plot(decade_avg.index, decade_avg['tempo'], marker='o', color='b')
plt.title('Темп (BPM) протягом десятиліть')
plt.xlabel('Десятиліття')
plt.ylabel('Темп (BPM)')
# Валентність
plt.subplot(3, 1, 2)
plt.plot(decade_avg.index, decade_avg['valence'], marker='o', color='g')
plt.title('Валентність (емоційна позитивність) протягом десятиліть')
plt.xlabel('Десятиліття')
plt.ylabel('Валентність')
# Гучність
plt.subplot(3, 1, 3)
plt.plot(decade_avg.index, decade_avg['loudness'], marker='o', color='r')
plt.title('Гучність (децибели) протягом десятиліть')
plt.xlabel('Десятиліття')
plt.ylabel('Гучність (dB)')
# Показуємо графіки
plt.tight_layout()