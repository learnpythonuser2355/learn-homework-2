import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


DATAS = [
    {'name': 'Alex', 'age': 20, 'job': 'Scientist'},
    {'name': 'Martin', 'age': 37, 'job': 'Programmer'},
    {'name': 'William', 'age': 15, 'job': 'Schoolboy '},
    {'name': 'Jacob', 'age': 8, 'job': 'Coolboy'}
]

def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for data in DATAS:
            writer.writerow(data)

if __name__ == "__main__":
    main()
