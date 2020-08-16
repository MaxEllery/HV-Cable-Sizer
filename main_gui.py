# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchForm(object):
    def setupUi(self, SearchForm):
        SearchForm.setObjectName("SearchForm")
        SearchForm.resize(1200, 559)
        SearchForm.setMinimumSize(QtCore.QSize(1200, 559))
        SearchForm.setMaximumSize(QtCore.QSize(1200, 559))
        self.manufacturer_comboBox = QtWidgets.QComboBox(SearchForm)
        self.manufacturer_comboBox.setGeometry(QtCore.QRect(260, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.manufacturer_comboBox.setFont(font)
        self.manufacturer_comboBox.setObjectName("manufacturer_comboBox")
        self.manufacturer_comboBox.addItem("")
        self.manufacturer_comboBox.setItemText(0, "")
        self.manufacturer_comboBox.addItem("")
        self.manufacturer_comboBox.addItem("")
        self.manufacturer_comboBox.addItem("")
        self.label = QtWidgets.QLabel(SearchForm)
        self.label.setGeometry(QtCore.QRect(10, 80, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.standard_comboBox = QtWidgets.QComboBox(SearchForm)
        self.standard_comboBox.setGeometry(QtCore.QRect(260, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.standard_comboBox.setFont(font)
        self.standard_comboBox.setObjectName("standard_comboBox")
        self.standard_comboBox.addItem("")
        self.standard_comboBox.setItemText(0, "")
        self.standard_comboBox.addItem("")
        self.standard_comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(SearchForm)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.voltage_comboBox = QtWidgets.QComboBox(SearchForm)
        self.voltage_comboBox.setGeometry(QtCore.QRect(260, 230, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltage_comboBox.setFont(font)
        self.voltage_comboBox.setObjectName("voltage_comboBox")
        self.voltage_comboBox.addItem("")
        self.voltage_comboBox.setItemText(0, "")
        self.voltage_comboBox.addItem("")
        self.voltage_comboBox.addItem("")
        self.voltage_comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(SearchForm)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SearchForm)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 221, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.CSA_comboBox = QtWidgets.QComboBox(SearchForm)
        self.CSA_comboBox.setGeometry(QtCore.QRect(260, 260, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CSA_comboBox.setFont(font)
        self.CSA_comboBox.setObjectName("CSA_comboBox")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.setItemText(0, "")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.CSA_comboBox.addItem("")
        self.reset_pushButton = QtWidgets.QPushButton(SearchForm)
        self.reset_pushButton.setGeometry(QtCore.QRect(810, 280, 151, 31))
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.search_pushButton = QtWidgets.QPushButton(SearchForm)
        self.search_pushButton.setGeometry(QtCore.QRect(610, 280, 151, 31))
        self.search_pushButton.setObjectName("search_pushButton")
        self.label_13 = QtWidgets.QLabel(SearchForm)
        self.label_13.setGeometry(QtCore.QRect(20, 10, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.layout_comboBox = QtWidgets.QComboBox(SearchForm)
        self.layout_comboBox.setGeometry(QtCore.QRect(260, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.layout_comboBox.setFont(font)
        self.layout_comboBox.setObjectName("layout_comboBox")
        self.layout_comboBox.addItem("")
        self.layout_comboBox.setItemText(0, "")
        self.layout_comboBox.addItem("")
        self.layout_comboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(SearchForm)
        self.label_14.setGeometry(QtCore.QRect(10, 140, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(SearchForm)
        self.label_15.setGeometry(QtCore.QRect(10, 170, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.material_comboBox = QtWidgets.QComboBox(SearchForm)
        self.material_comboBox.setGeometry(QtCore.QRect(260, 170, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.material_comboBox.setFont(font)
        self.material_comboBox.setObjectName("material_comboBox")
        self.material_comboBox.addItem("")
        self.material_comboBox.setItemText(0, "")
        self.material_comboBox.addItem("")
        self.material_comboBox.addItem("")
        self.label_16 = QtWidgets.QLabel(SearchForm)
        self.label_16.setGeometry(QtCore.QRect(10, 200, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.armour_comboBox = QtWidgets.QComboBox(SearchForm)
        self.armour_comboBox.setGeometry(QtCore.QRect(260, 200, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.armour_comboBox.setFont(font)
        self.armour_comboBox.setObjectName("armour_comboBox")
        self.armour_comboBox.addItem("")
        self.armour_comboBox.setItemText(0, "")
        self.armour_comboBox.addItem("")
        self.armour_comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(SearchForm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 320, 1181, 231))
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(16)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.label_5 = QtWidgets.QLabel(SearchForm)
        self.label_5.setGeometry(QtCore.QRect(450, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SearchForm)
        self.label_6.setGeometry(QtCore.QRect(450, 110, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(SearchForm)
        self.label_7.setGeometry(QtCore.QRect(450, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.power_textEdit = QtWidgets.QTextEdit(SearchForm)
        self.power_textEdit.setGeometry(QtCore.QRect(660, 80, 101, 21))
        self.power_textEdit.setObjectName("power_textEdit")
        self.pf_textEdit = QtWidgets.QTextEdit(SearchForm)
        self.pf_textEdit.setGeometry(QtCore.QRect(660, 110, 101, 21))
        self.pf_textEdit.setObjectName("pf_textEdit")
        self.vpu_textEdit = QtWidgets.QTextEdit(SearchForm)
        self.vpu_textEdit.setGeometry(QtCore.QRect(660, 140, 101, 21))
        self.vpu_textEdit.setObjectName("vpu_textEdit")
        self.label_8 = QtWidgets.QLabel(SearchForm)
        self.label_8.setGeometry(QtCore.QRect(810, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(SearchForm)
        self.label_9.setGeometry(QtCore.QRect(810, 110, 231, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.grouped_no_comboBox = QtWidgets.QComboBox(SearchForm)
        self.grouped_no_comboBox.setGeometry(QtCore.QRect(1100, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grouped_no_comboBox.setFont(font)
        self.grouped_no_comboBox.setObjectName("grouped_no_comboBox")
        self.grouped_no_comboBox.addItem("")
        self.grouped_no_comboBox.addItem("")
        self.grouped_no_comboBox.addItem("")
        self.grouped_no_comboBox.addItem("")
        self.grouped_no_comboBox.addItem("")
        self.grouped_no_comboBox.addItem("")
        self.grouped_spacing_comboBox = QtWidgets.QComboBox(SearchForm)
        self.grouped_spacing_comboBox.setGeometry(QtCore.QRect(1100, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grouped_spacing_comboBox.setFont(font)
        self.grouped_spacing_comboBox.setObjectName("grouped_spacing_comboBox")
        self.grouped_spacing_comboBox.addItem("")
        self.grouped_spacing_comboBox.addItem("")
        self.grouped_spacing_comboBox.addItem("")
        self.grouped_spacing_comboBox.addItem("")
        self.grouped_spacing_comboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(SearchForm)
        self.label_10.setGeometry(QtCore.QRect(810, 250, 281, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(SearchForm)
        self.label_11.setGeometry(QtCore.QRect(810, 220, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.thermal_res_comboBox = QtWidgets.QComboBox(SearchForm)
        self.thermal_res_comboBox.setGeometry(QtCore.QRect(1100, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thermal_res_comboBox.setFont(font)
        self.thermal_res_comboBox.setObjectName("thermal_res_comboBox")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.thermal_res_comboBox.addItem("")
        self.temp_comboBox = QtWidgets.QComboBox(SearchForm)
        self.temp_comboBox.setGeometry(QtCore.QRect(1100, 250, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temp_comboBox.setFont(font)
        self.temp_comboBox.setObjectName("temp_comboBox")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.temp_comboBox.addItem("")
        self.depth_comboBox = QtWidgets.QComboBox(SearchForm)
        self.depth_comboBox.setGeometry(QtCore.QRect(1100, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.depth_comboBox.setFont(font)
        self.depth_comboBox.setObjectName("depth_comboBox")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.depth_comboBox.addItem("")
        self.label_12 = QtWidgets.QLabel(SearchForm)
        self.label_12.setGeometry(QtCore.QRect(810, 190, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.current_textEdit = QtWidgets.QTextEdit(SearchForm)
        self.current_textEdit.setGeometry(QtCore.QRect(660, 250, 101, 21))
        self.current_textEdit.setObjectName("current_textEdit")
        self.label_17 = QtWidgets.QLabel(SearchForm)
        self.label_17.setGeometry(QtCore.QRect(450, 250, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.search_pushButton_2 = QtWidgets.QPushButton(SearchForm)
        self.search_pushButton_2.setGeometry(QtCore.QRect(660, 210, 101, 31))
        self.search_pushButton_2.setObjectName("search_pushButton_2")
        self.label_18 = QtWidgets.QLabel(SearchForm)
        self.label_18.setGeometry(QtCore.QRect(10, 290, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.installation_comboBox = QtWidgets.QComboBox(SearchForm)
        self.installation_comboBox.setGeometry(QtCore.QRect(260, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.installation_comboBox.setFont(font)
        self.installation_comboBox.setObjectName("installation_comboBox")
        self.installation_comboBox.addItem("")
        self.installation_comboBox.setItemText(0, "")
        self.installation_comboBox.addItem("")
        self.installation_comboBox.addItem("")
        self.installation_comboBox.addItem("")

        self.retranslateUi(SearchForm)
        QtCore.QMetaObject.connectSlotsByName(SearchForm)

    def retranslateUi(self, SearchForm):
        _translate = QtCore.QCoreApplication.translate
        SearchForm.setWindowTitle(_translate("SearchForm", "High Voltage Cable Size Calculator v0.1- by Max Ellery"))
        self.manufacturer_comboBox.setItemText(1, _translate("SearchForm", "Nexans"))
        self.manufacturer_comboBox.setItemText(2, _translate("SearchForm", "BICC"))
        self.manufacturer_comboBox.setItemText(3, _translate("SearchForm", "ElSewedey"))
        self.label.setText(_translate("SearchForm", "Manufacturer"))
        self.standard_comboBox.setItemText(1, _translate("SearchForm", "BS6622 / BS7835"))
        self.standard_comboBox.setItemText(2, _translate("SearchForm", "BS7870-4.10 / IEC60502"))
        self.label_2.setText(_translate("SearchForm", "Design Standard"))
        self.voltage_comboBox.setItemText(1, _translate("SearchForm", "6.6"))
        self.voltage_comboBox.setItemText(2, _translate("SearchForm", "11"))
        self.voltage_comboBox.setItemText(3, _translate("SearchForm", "33"))
        self.label_3.setText(_translate("SearchForm", "Voltage (kV)"))
        self.label_4.setText(_translate("SearchForm", "Cross Sectional Area (mm2)"))
        self.CSA_comboBox.setItemText(1, _translate("SearchForm", "25"))
        self.CSA_comboBox.setItemText(2, _translate("SearchForm", "35"))
        self.CSA_comboBox.setItemText(3, _translate("SearchForm", "50"))
        self.CSA_comboBox.setItemText(4, _translate("SearchForm", "70"))
        self.CSA_comboBox.setItemText(5, _translate("SearchForm", "95"))
        self.CSA_comboBox.setItemText(6, _translate("SearchForm", "120"))
        self.CSA_comboBox.setItemText(7, _translate("SearchForm", "150"))
        self.CSA_comboBox.setItemText(8, _translate("SearchForm", "185"))
        self.CSA_comboBox.setItemText(9, _translate("SearchForm", "240"))
        self.CSA_comboBox.setItemText(10, _translate("SearchForm", "300"))
        self.CSA_comboBox.setItemText(11, _translate("SearchForm", "400"))
        self.CSA_comboBox.setItemText(12, _translate("SearchForm", "500"))
        self.CSA_comboBox.setItemText(13, _translate("SearchForm", "630"))
        self.CSA_comboBox.setItemText(14, _translate("SearchForm", "800"))
        self.CSA_comboBox.setItemText(15, _translate("SearchForm", "1000"))
        self.reset_pushButton.setText(_translate("SearchForm", "Reset"))
        self.search_pushButton.setText(_translate("SearchForm", "Search"))
        self.label_13.setText(_translate("SearchForm", "High Voltage Cable Size Calculator"))
        self.layout_comboBox.setItemText(1, _translate("SearchForm", "Single Core"))
        self.layout_comboBox.setItemText(2, _translate("SearchForm", "Three Core"))
        self.label_14.setText(_translate("SearchForm", "Cable Layout"))
        self.label_15.setText(_translate("SearchForm", "Material"))
        self.material_comboBox.setItemText(1, _translate("SearchForm", "Copper"))
        self.material_comboBox.setItemText(2, _translate("SearchForm", "Aluminium"))
        self.label_16.setText(_translate("SearchForm", "Armour"))
        self.armour_comboBox.setItemText(1, _translate("SearchForm", "Armoured"))
        self.armour_comboBox.setItemText(2, _translate("SearchForm", "Unarmoured"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchForm", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchForm", "Manufacturer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchForm", "Standard"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchForm", "Layout"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SearchForm", "Material"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SearchForm", "Armour"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SearchForm", "Voltage (kV)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("SearchForm", "CSA (mm2)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("SearchForm", "Resistance (ohm/km)"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("SearchForm", "Inductance (mH/km)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("SearchForm", "Capacitance (uF/km)"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("SearchForm", "SC Rating Conductor (kA)"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("SearchForm", "SC Rating 50mm2 Screen (kA)"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("SearchForm", "Direct Buried Current Rating (A)"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("SearchForm", "Ducted Current Rating (A)"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("SearchForm", "Open Air Current Rating (A)"))
        self.label_5.setText(_translate("SearchForm", "Power on cable (MW)"))
        self.label_6.setText(_translate("SearchForm", "Power Factor"))
        self.label_7.setText(_translate("SearchForm", "Voltage (pu)"))
        self.pf_textEdit.setHtml(_translate("SearchForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.vpu_textEdit.setHtml(_translate("SearchForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_8.setText(_translate("SearchForm", "Grouped Cables"))
        self.label_9.setText(_translate("SearchForm", "Spacing of grouped cables (m)"))
        self.grouped_no_comboBox.setItemText(0, _translate("SearchForm", "1"))
        self.grouped_no_comboBox.setItemText(1, _translate("SearchForm", "2"))
        self.grouped_no_comboBox.setItemText(2, _translate("SearchForm", "3"))
        self.grouped_no_comboBox.setItemText(3, _translate("SearchForm", "4"))
        self.grouped_no_comboBox.setItemText(4, _translate("SearchForm", "5"))
        self.grouped_no_comboBox.setItemText(5, _translate("SearchForm", "6"))
        self.grouped_spacing_comboBox.setItemText(0, _translate("SearchForm", "0"))
        self.grouped_spacing_comboBox.setItemText(1, _translate("SearchForm", "0.15"))
        self.grouped_spacing_comboBox.setItemText(2, _translate("SearchForm", "0.3"))
        self.grouped_spacing_comboBox.setItemText(3, _translate("SearchForm", "0.45"))
        self.grouped_spacing_comboBox.setItemText(4, _translate("SearchForm", "0.6"))
        self.label_10.setText(_translate("SearchForm", "Ground Ambient Temperature (deg C)"))
        self.label_11.setText(_translate("SearchForm", "Soil Thermal Resistivity (K.m/W)"))
        self.thermal_res_comboBox.setItemText(0, _translate("SearchForm", "1.2"))
        self.thermal_res_comboBox.setItemText(1, _translate("SearchForm", "0.8"))
        self.thermal_res_comboBox.setItemText(2, _translate("SearchForm", "0.9"))
        self.thermal_res_comboBox.setItemText(3, _translate("SearchForm", "1"))
        self.thermal_res_comboBox.setItemText(4, _translate("SearchForm", "1.5"))
        self.thermal_res_comboBox.setItemText(5, _translate("SearchForm", "2"))
        self.thermal_res_comboBox.setItemText(6, _translate("SearchForm", "2.5"))
        self.temp_comboBox.setItemText(0, _translate("SearchForm", "15"))
        self.temp_comboBox.setItemText(1, _translate("SearchForm", "20"))
        self.temp_comboBox.setItemText(2, _translate("SearchForm", "25"))
        self.temp_comboBox.setItemText(3, _translate("SearchForm", "30"))
        self.temp_comboBox.setItemText(4, _translate("SearchForm", "35"))
        self.temp_comboBox.setItemText(5, _translate("SearchForm", "40"))
        self.temp_comboBox.setItemText(6, _translate("SearchForm", "45"))
        self.depth_comboBox.setItemText(0, _translate("SearchForm", "0.8"))
        self.depth_comboBox.setItemText(1, _translate("SearchForm", "0.5"))
        self.depth_comboBox.setItemText(2, _translate("SearchForm", "0.6"))
        self.depth_comboBox.setItemText(3, _translate("SearchForm", "1"))
        self.depth_comboBox.setItemText(4, _translate("SearchForm", "1.25"))
        self.depth_comboBox.setItemText(5, _translate("SearchForm", "1.5"))
        self.depth_comboBox.setItemText(6, _translate("SearchForm", "1.75"))
        self.depth_comboBox.setItemText(7, _translate("SearchForm", "2"))
        self.depth_comboBox.setItemText(8, _translate("SearchForm", "2.5"))
        self.depth_comboBox.setItemText(9, _translate("SearchForm", "3"))
        self.label_12.setText(_translate("SearchForm", "Burial Depth (m)"))
        self.current_textEdit.setHtml(_translate("SearchForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("SearchForm", "Full Load Current"))
        self.search_pushButton_2.setText(_translate("SearchForm", "Calculate Current"))
        self.label_18.setText(_translate("SearchForm", "Installation Method"))
        self.installation_comboBox.setItemText(1, _translate("SearchForm", "Direct Buried"))
        self.installation_comboBox.setItemText(2, _translate("SearchForm", "Ducted"))
        self.installation_comboBox.setItemText(3, _translate("SearchForm", "Open Air"))