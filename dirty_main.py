# Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции (необязательное задание)

from main import *

# print(datetime.now().replace(microsecond=0))

if __name__ == '__main__':

    get_employees()
    calculate_salary()