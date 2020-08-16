from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
from main_gui import Ui_SearchForm
import sqlite3
from sqlite3 import Error
from math import *

def sql_connection():
    try:
        conn = sqlite3.connect('database_test.db')
        return conn
    except Error:
        print(Error)


class searchWindow(QMainWindow, Ui_SearchForm):
    def __init__(self):
        super(searchWindow, self).__init__()
        self.setupUi(self)
        self.search_pushButton.clicked.connect(self.search_connection)
        self.search_pushButton_2.clicked.connect(self.calculate_current)

    def search_connection(self):
        try:
            # table_headers = ['manufacturer',
            #                           'standard',
            #                           'layout',
            #                           'material',
            #                           'armour',
            #                           'voltage',
            #                           'CSA',
            #                           'resistance',
            #                           'inductance',
            #                           'capacitance',
            #                           'sc_conductor',
            #                           'sc_screen',
            #                           'current_directburied',
            #                           'current_ducts',
            #                           'current_open']
            self.tableWidget.clear()
            self.tableWidget.setRowCount(1)
            # for i in range(len(table_headers)):
            #     header_data = QTableWidgetItem(str(table_headers[i]))
            #     self.tableWidget.setItem(0, i, header_data)
            full_load_current = float(self.current_textEdit.toPlainText())
            query = (full_load_current, full_load_current, full_load_current)
            conn = sql_connection()
            cursorObj = conn.cursor()
            query_result =  cursorObj.execute(
                    'SELECT * FROM cables WHERE CAST(current_directburied as INTEGER) > ? OR CAST(current_ducts as INTEGER) > ? OR CAST(current_open as INTEGER) > ?', query)
            for row_number, i in enumerate(query_result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(i):
                    cell_data = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number, cell_data)

            conn.close()
        except:
            return

    def calculate_current(self):
        try:
            voltage = float(self.voltage_comboBox.currentText()) * 1000
            power = float(self.power_textEdit.toPlainText()) * 1000000
            vpu = float(self.vpu_textEdit.toPlainText())

            current = round(power / (sqrt(3) * voltage * vpu), 2)
            self.current_textEdit.setText(str(current))
        except:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = searchWindow()
    w.show()
    sys.exit(app.exec_())
