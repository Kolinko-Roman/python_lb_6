# Завдання 1

def skarbnytsia_korolia():
    try:
        coins = int(input("Введіть кількість золотих монет (1-1000): "))
        people = int(input("Скільки людей у команді? "))

        share = coins // people
        print(f"Кожен отримує {share} монет.")
    
    except ValueError:
        print("Помилка: введіть числове значення!")
    except ZeroDivisionError:
        print("Помилка: не можна ділити на нуль!")
    finally:
        print("Пригоди тривають!")

skarbnytsia_korolia()


# Завдання 2

import random

def kod_seifu():
    code = random.randint(100, 999)
    attempts = 5

    print("Ви маєте 5 спроб зламати код сейфу!")

    while attempts > 0:
        try:
            guess = int(input("Введіть тризначний код: "))
            
            if guess == code:
                print("Вітаю! Ви зламали сейф!")
                return
            elif guess < code:
                print("Код більший.")
            else:
                print("Код менший.")

            attempts -= 1
            print(f"Залишилось спроб: {attempts}")

        except ValueError:
            print("Помилка: введіть число!")

    print(f"Спроби вичерпано! Код був: {code}")

kod_seifu()


# Завдання 3

import random

choices = ["камінь", "ножиці", "папір", "ящірка", "Спок"]
rules = {
    "камінь": ["ножиці", "ящірка"],
    "ножиці": ["папір", "ящірка"],
    "папір": ["камінь", "Спок"],
    "ящірка": ["папір", "Спок"],
    "Спок": ["ножиці", "камінь"]
}

def rpsls():
    computer = random.choice(choices)
    try:
        player = input("Виберіть: камінь, ножиці, папір, ящірка, Спок: ").strip()

        if player not in choices:
            raise ValueError("Некоректний вибір!")

        print(f"Комп'ютер вибрав: {computer}")

        if player == computer:
            print("Нічия!")
        elif computer in rules[player]:
            print("Ви виграли!")
        else:
            print("Ви програли!")

    except ValueError as e:
        print(f"Помилка: {e}")

rpsls()


# Завдання 4

def bonus_system():
    try:
        points = int(input("Введіть кількість очок (0-100): "))

        if points < 0 or points > 100:
            raise ValueError("Некоректне введення! Кількість очок повинна бути в межах 0-100.")

        if points < 50:
            rank, multiplier = "Початківець", 1
        elif points < 70:
            rank, multiplier = "Срібний гравець", 1.5
        elif points < 90:
            rank, multiplier = "Золотий гравець", 2
        else:
            rank, multiplier = "Платиновий гравець", 3

        final_score = points * multiplier
        print(f"Ваш рейтинг: {rank}! Ви отримали {final_score} балів (множник ×{multiplier})!")

    except ValueError as e:
        print(f"Помилка: {e}")


bonus_system()


# Завдання 5

import random

def escape_island():
    try:
        wood = int(input("Скільки деревини для плоту? (1-10): "))
        if wood < 3:
            print("Деревини замало, пліт затонув! Гру завершено.")
            return

        action = input("Як тікати від піратів? (бігти, сховатися, битися): ").strip().lower()
        if action not in ["бігти", "сховатися", "битися"]:
            raise ValueError("Такого варіанту немає, пірати вас спіймали!")

        chest_code = random.randint(10, 99)
        guess = int(input("Введіть двозначний код, щоб відкрити скриню: "))
        if guess != chest_code:
            print("Неправильний код, скриня вибухнула! Гру завершено.")
            return

        print("Скарб ваш, ви врятовані!")

    except ValueError as e:
        print(f"Помилка: {e}")

    finally:
        print("Гра завершена. Дякуємо за участь у пригоді!")

escape_island()
