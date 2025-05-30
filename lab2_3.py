# Демонстрация работы модуля math_operations

import math_operations

def main():
    a = 10
    b = 5
    c = 0

    print("Сумма (10 + 5):", math_operations.add(a, b))
    print("Разность (10 - 5):", math_operations.subtract(a, b))
    print("Произведение (10 * 5):", math_operations.multiply(a, b))
    print("Деление (10 / 5):", math_operations.divide(a, b))
    print("Деление на ноль (10 / 0):", math_operations.divide(a, c))

if __name__ == '__main__':
    main()
