"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Введите число целое положительное число n: ")
nn = str(n) * 2
nnn = str(n) * 3
result = int(n) + int(nn) + int(nnn)
print(f"Сумма чисел n + nn + nnn: {result}")
