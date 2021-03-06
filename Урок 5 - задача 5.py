# Задача № 5: Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#             Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
# Решение:

# сумма введенного набора чисел
summa = 0

print('Формат ввода данных: необходимо ввести набор из целых чисел, разделенные пробелами')

# with ... as - менеджеры контекста, более удобная форма для работы с файлами (и не только)
# with ... as - сам откроет и закроет файл, а если будет ошибка
# open() - выполняется открытие файла, который будет указан в аргументах (в скобках)
# w+ - открывает/создает файл как для записи, так и для чтения
# file - переменная, которая будет ссылаться на объект файла
with open('tasks_5.txt', 'w+', encoding='utf-8') as file:
    text = input('Введите, пожалуйста, набор чисел: ')
    # записываем в файл введенную строку из набора целых чисел
    file.writelines(text)
    # заносим в переменную введенную строку из набора целых чисел в виде списка
    number_list = text.split()

# идем по списку, преобразуем каждый элемент списка в тип данных integer (целое число)
for i in number_list:
    summa += int(i)

print(f'Сумма введенных чисел = {summa}')
