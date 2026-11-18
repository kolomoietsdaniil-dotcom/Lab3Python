import random

import random

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, 5))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def row_product(row):
    num = 1
    for i in row:
        num *= i
    return num

def transform_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(0, n - i - 1):
            if row_product(matrix[j]) > row_product(matrix[j + 1]):
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]
def task1():
    n = int(input("Введіть розмірність матриці (n): "))
    while n > 15:
        print("Розмірність матриці не повинна перевищувати 15.")
        n = int(input("Введіть розмірність матриці (n): "))
    matrix = create_matrix(n)
    print("Початкова матриця:")
    print_matrix(matrix)
    
    transform_matrix(matrix)
    
    print("Матриця після сортування рядків за добутком елементів:")
    print_matrix(matrix)

def task2():

    teams_data = {
    "Шахтар": 72,
    "ЛНЗ": 60,
    "Полісся": 59,
    "Динамо": 57,
    "Харків": 51,
    "Колос": 49,
    "Кривбас": 48,
    "Зоря": 46,
    "Карпати": 41,
    "Епіцентр": 32
    }

    first_place_points = 0
    first_place_team = ""
    second_place_points = 0
    second_place_team = ""
    third_place_points = 0
    third_place_team = ""

    for team, points in teams_data.items():
        if points > first_place_points:
            third_place_points = second_place_points
            third_place_team = second_place_team
            second_place_points = first_place_points
            second_place_team = first_place_team
            first_place_points = points
            first_place_team = team
        elif points > second_place_points:
            third_place_points = second_place_points
            third_place_team = second_place_team
            second_place_points = points
            second_place_team = team
        elif points > third_place_points:
            third_place_points = points
            third_place_team = team
  

    print(f"Чемпіон: {first_place_team}")
    print(f"Друга {second_place_team} та третя {third_place_team} команди.")
    print(f"Перша {first_place_team} та друга {second_place_team} команди.")

def task3():
    synonymus = {
    }

    N = int(input("Введіть кількість слів: "))
    for i in range(N):
        word1, word2 = input(f"Введіть пару слів (слово1 слово2) для слова {i + 1}: ").split()
        synonymus[word1] = word2
        synonymus[word2] = word1

    target_word = input("Введіть слово: ")
    print(synonymus[target_word])
  
while True:
    print("\n ГОЛОВНЕ МЕНЮ ")
    print("1 Завдання")
    print("2 Завдання ")
    print("3 Завдання ")
    print("0. Вийти з програми")
    
    choice = input("Оберіть пункт меню: ")
    
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2, 3 або 0.")