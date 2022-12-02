#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]
        self.plainTextEdit.setPlainText("")
        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.readlines()

            global list_of_numbers
            list_of_numbers = []

            for lines in data:
                lineSplit = lines.split()
                list_of_numbers.append(lineSplit)

            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: \n")

            for lines in data:
                lines.strip('\n')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:5}".format(str(i))
                    self.plainTextEdit.insertPlainText(new_str)
                self.plainTextEdit.insertPlainText("\n")



    def process_data(self):
        if validation_of_data():
            max_i_1 = find_max_1()
            max_i_2 = find_max_2()

            count = 0
            # for i in range(len(list_of_numbers)):
            for j in range(len(list_of_numbers[2])):
                if int(list_of_numbers[2][j]) == 1:
                    count += 1
            if count == 5:
                list_of_numbers[max_i_1][0] = str(int(list_of_numbers[max_i_1][0]) * 2)
                list_of_numbers[max_i_2][1] = str(int(list_of_numbers[max_i_2][1]) * 3)
                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')
            else:
                self.plainTextEdit.appendPlainText("Данные не обработаны! " + '\n')

            # выводим список на экран
            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:5}".format(str(i))
                    self.plainTextEdit.insertPlainText(new_str)
                    # чтобы текст был в виде таблицы, делаем отступ после
                    # 6 элемента

                self.plainTextEdit.appendPlainText("")
            # else:
            #     self.plainTextEdit.appendPlainText(
            #         "Минимальный элемент не во втором столбце! \n")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """

        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for lists in list_of_numbers:
                for i in lists:
                    new_str = "{:6}".format(str(i))
                    file.write(new_str)
                file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_max_1():
    """
    находим максимальное число в списке
    :return: максимальное число
    """
    max_num = int(list_of_numbers[0][0])
    max_i_1 = 0
    for i in range(len(list_of_numbers)):
        if max_num < int(list_of_numbers[i][0]):
            max_num = int(list_of_numbers[i][0])
            max_i_1 = i
    return max_i_1

def find_max_2():
    """
    находим максимальное число в списке
    :return: максимальное число
    """
    max_num_2 = int(list_of_numbers[0][1])
    max_i_2 = 0
    for i in range(len(list_of_numbers)):
        if max_num_2 < int(list_of_numbers[i][1]):
            max_num_2 = int(list_of_numbers[i][1])
            max_i_2 = i
    return max_i_2


def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    lenth_list = 0
    for lists in list_of_numbers:
        lenth_list += len(lists)
    if lenth_list == 30:
        for lists in list_of_numbers:
            for i in lists:
                try:
                    int(i)
                except Exception:
                    return False
        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
