# lab2_task6.py
# Программа читает текст из файла text.txt, находит все даты в формате DD.MM.YYYY,
# преобразует их в формат YYYY-MM-DD, сохраняет результат в файл dates.txt,
# а затем сортирует даты по возрастанию с использованием лямбда-функций и выводит их.

import re
from datetime import datetime


def main():
    try:
        with open('text1.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл text1.txt не найден.")
        return

    # Регулярное выражение для поиска дат в формате DD.MM.YYYY
    date_pattern = r'\b(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[0-2])\.(\d{4})\b'
    matches = re.findall(date_pattern, text)

    converted_dates = []
    for day, month, year in matches:
        # Приводим день и месяц к двухзначному формату
        day = day.zfill(2)
        month = month.zfill(2)
        # Преобразуем в формат YYYY-MM-DD
        date_str = f"{year}-{month}-{day}"
        try:
            # Проверяем корректность даты
            datetime.strptime(date_str, "%Y-%m-%d")
            converted_dates.append(date_str)
        except ValueError:
            continue

    # Записываем преобразованные даты в файл dates.txt
    with open('dates.txt', 'w', encoding='utf-8') as file:
        file.write("\n".join(converted_dates))

    # Сортировка дат по возрастанию с использованием лямбда-функции
    sorted_dates = sorted(converted_dates, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))

    print("Отсортированные даты:")
    for date in sorted_dates:
        print(date)


if __name__ == '__main__':
    main()
