from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from input_gui import Ui_InputForm
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except Error:
        print(Error)


class inputWindow(QMainWindow, Ui_InputForm):
    def __init__(self):
        super(inputWindow, self).__init__()
        self.setupUi(self)
        self.insert_pushButton.clicked.connect(self.insert_to_database)
        self.reset_pushButton.clicked.connect(self.reset)


    def insert_to_database(self):
        conn = sql_connection()
        cursorObj = conn.cursor()
        cursorObj.execute("INSERT INTO cables (manufacturer, "
                          "standard, "
                          "voltage, "
                          "CSA, "
                          "resistance, "
                          "inductance, "
                          "capacitance, "
                          "sc_conductor, "
                          "sc_screen, "
                          "current_directburied, "
                          "current_ducts, "
                          "current_open) VALUES ('" + str(self.manufacturer_comboBox.currentText())
                          + str(self.standard_comboBox.currentText()) + "', '"
                          + str(self.voltage_comboBox.currentText()) + "', '"
                          + str(self.CSA_comboBox.currentText()) + "', '"
                          + str(self.resistance_lineEdit.text()) + "', '"
                          + str(self.inductance_lineEdit.text()) + "', '"
                          + str(self.capacitance_lineEdit.text()) + "', '"
                          + str(self.sc_conductor_lineEdit.text()) + "', '"
                          + str(self.sc_screen_lineEdit.text()) + "', '"
                          + str(self.current_direct_lineEdit.text()) + "', '"
                          + str(self.current_ducted_lineEdit.text()) + "', '"
                          + str(self.curren_open_lineEdit.text()) + "')")
        conn.close()


    def reset(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = inputWindow()
    w.show()
    sys.exit(app.exec_())
