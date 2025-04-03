# lab2_task2.py
# Программа запрашивает у пользователя два числа и делит первое число на второе.
# Обрабатываются исключения: деление на ноль и ввод нечисловых значений.

def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except ValueError:
        print("Ошибка: введены нечисловые значения.")
    else:
        print(f"Результат деления: {result}")

if __name__ == '__main__':
    main()
