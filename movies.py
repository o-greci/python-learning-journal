# Мой первый скрипт для портфолио
# Список любимых фильмов

# 1. Создаю список из 5 любимых фильмов
movies = ["Начало", "Матрица", "Зеленая книга", "Интерстеллар", "Форрест Гамп"]

# 2. Добавляю в конец еще один фильм
movies.append("Побег из Шоушенка")

# 3. Вывожу все фильмы с нумерацией
print("Мои любимые фильмы:")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# 4. Записываю список в файл
with open('movies.txt', 'w', encoding='utf-8') as f:
    for movie in movies:
        f.write(movie + '\n')

# 5. Читаю файл обратно и вывожу
print("\nФильмы из файла movies.txt:")
with open('movies.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())