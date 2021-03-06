# Задача № 4: Создать (не программно) текстовый файл со следующим содержимым:
#             One — 1
#             Two — 2
#             Three — 3
#             Four — 4
#             Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#             При этом английские числительные должны заменяться на русские.
#             Новый блок строк должен записываться в новый текстовый файл.
# Решение:

# создаем словарь, где по условию английские числительные необходимо заменить на русские числительные
translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_data = []  # измененные данные в виде списка, для записи в новый файл
old_file = 'tasks_4.txt'

# открываем файл в режиме чтения
file = open(old_file, 'r', encoding='utf-8')

print('Файл имеет следующие данные:')
# идем по файлу построчно
for old_data in file.readlines():
    # убираем 'перевод каретки'
    old_data = old_data.replace('\n', '')

    print(old_data)

    # разбиваем строку по символам ' ' формируя список,
    # 1 - означает сколько будет элементов в создаваем списке --> будет 2 т.к. 0 элемент и 1 элемент
    # где 0 элемент списка будет английские числительные, а 1 элемент списка будет все остальное
    old_data = old_data.split(' ', 1)

    # translation[old_data[0]] - это ключ словаря
    # old_data[1] - это так называемое все остальное
    # вставляем в список ключ словаря + пробел + все остальное
    new_data.append(translation[old_data[0]] + ' ' + old_data[1])

file.close()

# новый файл
new_file = 'tasks_4_1.txt'

# открываем файл в режиме записи
file = open(new_file, 'w', encoding='utf-8')

# исходя из длины списка с новыми данными, записываем каждый элемент списка в новую строку нового файла
for i in range(len(new_data)):
    file.writelines(new_data[i] + '\n')

file.close()
