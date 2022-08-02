from Translet_GUI import Ui_MainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from translate import Translator
from random import randint

from Spiski_lan import spiski_lag

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_exit.clicked.connect(QCoreApplication.instance().quit)
        self.ui.pushButton_translet.clicked.connect(self.translat)
        self.ui.pushButton_perer.clicked.connect(self.obmen)
        self.ui.pushButton_copy.clicked.connect(self.copy_in_buffer)

        self.input_data()

    def input_data(self):
        self.spis_lag = spiski_lag()

        for i in self.spis_lag.keys():
            self.ui.comboBox_with_lag.addItem(i)
            self.ui.comboBox_in_lag.addItem(i)

        self.ui.comboBox_in_lag.setCurrentIndex(randint(1, len(self.spis_lag)))

    def translat(self):
        text = self.ui.textEdit_translet_with.toPlainText()

        if text == "":
            self.msg("Error", "Введите текст в поле для перевода!")
        else:    
            lag_with = self.spis_lag.get(self.ui.comboBox_with_lag.currentText())
            lag_in = self.spis_lag.get(self.ui.comboBox_in_lag.currentText())

            tr = Translator(to_lang=lag_in, from_lang=lag_with)
            self.ui.textEdit_translet_in.setText(tr.translate(text))

    def obmen(self):
        lag = self.ui.comboBox_with_lag.currentIndex()

        self.ui.comboBox_with_lag.setCurrentIndex(self.ui.comboBox_in_lag.currentIndex())
        self.ui.comboBox_in_lag.setCurrentIndex(lag)
        self.ui.textEdit_translet_with.setText(self.ui.textEdit_translet_in.toPlainText())
        self.ui.textEdit_translet_in.setText("")

    def copy_in_buffer(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.textEdit_translet_in.toPlainText())
        self.msg("Information", "Перевод сохранён в буффер!")

    def msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if reson == "Information":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()