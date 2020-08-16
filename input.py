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

def sql_insert_cabledata(manufacturer,
                         standard,
                         layout,
                         material,
                         armour,
                         voltage,
                         CSA,
                         resistance,
                         inductance,
                         capacitance,
                         sc_conductor,
                         sc_screen,
                         current_directburied,
                         current_ducts,
                         current_open):
    conn = sql_connection()
    cursorObj = conn.cursor()
    sql_query = '''INSERT INTO cables (
                           manufacturer, 
                           standard,
                           layout, 
                           material, 
                           armour,  
                           voltage, 
                           CSA, 
                           resistance, 
                           inductance, 
                           capacitance, 
                           sc_conductor, 
                           sc_screen, 
                           current_directburied, 
                           current_ducts, 
                           current_open
                        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    '''
    cursorObj.execute(sql_query, (manufacturer,
                                  standard,
                                  layout,
                                  material,
                                  armour,
                                  voltage,
                                  CSA,
                                  resistance,
                                  inductance,
                                  capacitance,
                                  sc_conductor,
                                  sc_screen,
                                  current_directburied,
                                  current_ducts,
                                  current_open))
    conn.commit()
    conn.close()


class inputWindow(QMainWindow, Ui_InputForm):
    def __init__(self):
        super(inputWindow, self).__init__()
        self.setupUi(self)
        self.insert_pushButton.clicked.connect(self.insert_to_database)
        self.reset_pushButton.clicked.connect(self.reset)


    def insert_to_database(self):
        sql_insert_cabledata(self.manufacturer_comboBox.currentText(),
                   self.standard_comboBox.currentText(),
                   self.layout_comboBox.currentText(),
                   self.material_comboBox.currentText(),
                   self.armour_comboBox.currentText(),
                   self.voltage_comboBox.currentText(),
                   self.CSA_comboBox.currentText(),
                   self.resistance_lineEdit.text(),
                   self.inductance_lineEdit.text(),
                   self.capacitance_lineEdit.text(),
                   self.sc_conductor_lineEdit.text(),
                   self.sc_screen_lineEdit.text(),
                   self.current_direct_lineEdit.text(),
                   self.current_ducted_lineEdit.text(),
                   self.current_open_lineEdit.text())


    def reset(self):
        self.resistance_lineEdit.setText("")
        self.inductance_lineEdit.setText("")
        self.capacitance_lineEdit.setText("")
        self.sc_conductor_lineEdit.setText("")
        self.sc_screen_lineEdit.setText("")
        self.current_ducted_lineEdit.setText("")
        self.current_direct_lineEdit.setText("")
        self.curren_open_lineEdit.setText("")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = inputWindow()
    w.show()
    sys.exit(app.exec_())
