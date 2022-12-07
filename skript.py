#!/usr/bin/python3
import math
import cmath

# Задание 1.

point = [0, 0]
step = int(input("Введите количество шагов: "))
while step < 0:
    step = int(input("Ошибка формата. Попробуйте ещё раз: "))
action = int(input("Введите направление(1 - вправо, 2 - вверх, 3 - влево, 4 - вниз: "))
if action == 1:
    point[0] += step
elif action == 2:
    point[1] += step
elif action == 3:
    point[0] -= step
elif action == 4:
    point[1] -= step
else:
    print("Неверное направление.")
print("Ваши координаты: x:", point[0], "y:", point[1])


# Задание 2.

def moving():
    global action
    global point
    if action == 1:
        point[0] += step
    elif action == 2:
        point[1] += step
    elif action == 3:
        point[0] -= step
    elif action == 4:
        point[1] -= step
    else:
        return False
    return True


point = [0, 0]
while True:
    step = int(input("Введите количество шагов (0 - закончить): "))
    while step < 0:
        step = int(input("Ошибка формата. Попробуйте ещё раз: "))
    if step == 0:
        break
    action = int(input("Введите направление(1 - вправо, 2 - вверх, 3 - влево, 4 - вниз, иная цифра - закончить: "))
    if not moving():
        break
print("Ваши координаты: x:", point[0], "y:", point[1])

# Задание 3.

print("Квадратное уравнение: ax^2 + bx + c = 0")
a = float(input("Введите коэффициент а квадратного уравнения: "))
b = float(input("Введите коэффициент b квадратного уравнения: "))
c = float(input("Введите коэффициент c квадратного уравнения: "))
D = b ** 2 - 4 * a * c
print("Ваше квадратное уравнение:")
print(str(a) + " * x^2 + " + str(b) + " * x + " + str(c) + " = 0")
print("Дискриминант:", D)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Корни уравнения: x1 =", x1, "x2 =", x2)
elif D == 0:
    x = -b / (2 * a)
    print("Корень уравнения: x1 =", x)
else:
    print("Корней нет")

# Задание 4.

print("Квадратное уравнение: ax^2 + bx + c = 0")
usr_choice = int(input("Какие коэффициенты вы хотите вводить? (1 - действительные, 2 - комплексные): "))
while usr_choice not in {1, 2}:
    usr_choice = int(input("Ошибка формата. Попробуйте снова (1 - действительные, 2 - комплексные): "))
if usr_choice == 1:
    a = float(input("Введите коэффициент а квадратного уравнения: "))
    b = float(input("Введите коэффициент b квадратного уравнения: "))
    c = float(input("Введите коэффициент c квадратного уравнения: "))
else:
    print("Формат ввода: действительная часть пробел мнимая часть.")
    a = input("Введите коэффициент а квадратного уравнения: ").split(" ")
    a = complex(float(a[0]), float(a[1]))
    b = input("Введите коэффициент b квадратного уравнения: ").split(" ")
    b = complex(float(b[0]), float(b[1]))
    c = input("Введите коэффициент c квадратного уравнения: ").split(" ")
    c = complex(float(c[0]), float(c[1]))
D = pow(b, 2) - 4 * a * c
x1 = (-b + cmath.sqrt(D)) / (2 * a)
x2 = (-b - cmath.sqrt(D)) / (2 * a)
print("Ваше квадратное уравнение:")
print(str(a) + " * x^2 + " + str(b) + " * x + " + str(c) + " = 0")
print("Дискриминант:", D)
if usr_choice == 2:
    if D == 0:
        print("Корень уравнения: x1 =", x1)
    else:
        print("Корни уравнения: x1 =", x1, "x2 =", x2)
else:
    if D > 0:
        print("Корни уравнения: x1 =", x1.real, "x2 =", x2.real)
    elif D == 0:
        print("Корень уравнения: x1 =", x1.real)
    else:
        print("Корни уравнения: x1 =", x1, "x2 =", x2)
