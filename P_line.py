import sys
import os
import math
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("EVOL")
        MainWindow.resize(1070, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 760, 340))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ya.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        rx = QtCore.QRegExp("[0-9]{4}")
        val = QtGui.QRegExpValidator(rx)

        self.inputB = ClickableLineEdit(self.centralwidget)
        self.inputB.setGeometry(QtCore.QRect(150, 30, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputB.setFont(font)
        self.inputB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputB.setAlignment(QtCore.Qt.AlignCenter)
        self.inputB.setObjectName("inputB")
        # self.inputB.setText('0')
        self.inputB.setValidator(val)
        self.inputB.clicked.connect(self.inputB.clear)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.inputA = ClickableLineEdit(self.centralwidget)
        self.inputA.setGeometry(QtCore.QRect(150, 80, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputA.setFont(font)
        self.inputA.setAlignment(QtCore.Qt.AlignCenter)
        self.inputA.setObjectName("inputA")
        # self.inputA.setText('0')
        self.inputA.setValidator(val)
        self.inputA.clicked.connect(self.inputA.clear)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.inputC = ClickableLineEdit(self.centralwidget)
        self.inputC.setGeometry(QtCore.QRect(150, 130, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputC.setFont(font)
        self.inputC.setAlignment(QtCore.Qt.AlignCenter)
        self.inputC.setObjectName("inputC")
        self.inputC.setValidator(val)
        # self.inputC.setText('0')
        self.inputC.clicked.connect(self.inputC.clear)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.radioB = QtWidgets.QRadioButton(self.centralwidget)
        self.radioB.setGeometry(QtCore.QRect(10, 230, 64, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioB.setFont(font)
        self.radioB.setObjectName("radioB")

        self.radioE = QtWidgets.QRadioButton(self.centralwidget)
        self.radioE.setGeometry(QtCore.QRect(90, 230, 34, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioE.setFont(font)
        self.radioE.setObjectName("radioE")

        self.radioEB = QtWidgets.QRadioButton(self.centralwidget)
        self.radioEB.setGeometry(QtCore.QRect(150, 230, 45, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioEB.setFont(font)
        self.radioEB.setObjectName("radioEB")

        self.radioBC = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBC.setGeometry(QtCore.QRect(210, 230, 45, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioBC.setFont(font)
        self.radioBC.setObjectName("radioBC")

        self.Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.calculation())
        self.Button.setGeometry(QtCore.QRect(80, 280, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Button.setFont(font)
        self.Button.setObjectName("Button")

        self.A1 = QtWidgets.QLabel(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(400, 30, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A1.setFont(font)
        self.A1.setStyleSheet("QLabel{background-color: white;}")
        self.A1.setTextFormat(QtCore.Qt.AutoText)
        self.A1.setAlignment(QtCore.Qt.AlignCenter)
        self.A1.setObjectName("A1")

        self.B1 = QtWidgets.QLabel(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(570, 30, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B1.setFont(font)
        self.B1.setStyleSheet("QLabel{background-color: white;}")
        self.B1.setTextFormat(QtCore.Qt.AutoText)
        self.B1.setAlignment(QtCore.Qt.AlignCenter)
        self.B1.setObjectName("B1")

        self.A2 = QtWidgets.QLabel(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(730, 30, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.A2.setFont(font)
        self.A2.setStyleSheet("QLabel{background-color: white;}")
        self.A2.setTextFormat(QtCore.Qt.AutoText)
        self.A2.setAlignment(QtCore.Qt.AlignCenter)
        self.A2.setObjectName("A2")

        self.B2 = QtWidgets.QLabel(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(900, 30, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B2.setFont(font)
        self.B2.setStyleSheet("QLabel{background-color: white;}")
        self.B2.setTextFormat(QtCore.Qt.AutoText)
        self.B2.setAlignment(QtCore.Qt.AlignCenter)
        self.B2.setObjectName("B2")

        self.L = QtWidgets.QLabel(self.centralwidget)
        self.L.setGeometry(QtCore.QRect(660, 5, 60, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.L.setFont(font)
        self.L.setStyleSheet("QLabel{background-color: white;}")
        self.L.setTextFormat(QtCore.Qt.AutoText)
        self.L.setAlignment(QtCore.Qt.AlignCenter)
        self.L.setObjectName("L")

        self.K = QtWidgets.QLabel(self.centralwidget)
        self.K.setGeometry(QtCore.QRect(290, 100, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.K.setFont(font)
        self.K.setStyleSheet("QLabel{background-color: white;}")
        self.K.setTextFormat(QtCore.Qt.AutoText)
        self.K.setAlignment(QtCore.Qt.AlignCenter)
        self.K.setObjectName("K")

        self.C = QtWidgets.QLabel(self.centralwidget)
        self.C.setGeometry(QtCore.QRect(290, 185, 50, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.C.setFont(font)
        self.C.setStyleSheet("QLabel{background-color: white;}")
        self.C.setTextFormat(QtCore.Qt.AutoText)
        self.C.setAlignment(QtCore.Qt.AlignCenter)
        self.C.setObjectName("C")

        self.W = QtWidgets.QLabel(self.centralwidget)
        self.W.setGeometry(QtCore.QRect(1010, 185, 55, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.W.setFont(font)
        self.W.setStyleSheet("QLabel{background-color: white;}")
        self.W.setTextFormat(QtCore.Qt.AutoText)
        self.W.setAlignment(QtCore.Qt.AlignCenter)
        self.W.setObjectName("W")

        self.BplusA = QtWidgets.QLabel(self.centralwidget)
        self.BplusA.setGeometry(QtCore.QRect(510, 100, 172, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BplusA.setFont(font)
        self.BplusA.setStyleSheet("QLabel{background-color: white;}")
        self.BplusA.setTextFormat(QtCore.Qt.AutoText)
        self.BplusA.setAlignment(QtCore.Qt.AlignCenter)
        self.BplusA.setObjectName("BplusA")

        self.B_A = QtWidgets.QLabel(self.centralwidget)
        self.B_A.setGeometry(QtCore.QRect(370, 185, 125, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_A.setFont(font)
        self.B_A.setStyleSheet("QLabel{background-color: white;}")
        self.B_A.setTextFormat(QtCore.Qt.AutoText)
        self.B_A.setAlignment(QtCore.Qt.AlignCenter)
        self.B_A.setObjectName("B_A")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 350, 116, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(420, 350, 621, 70))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(415, 340, 610, 70))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.comment = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.comment.setGeometry(QtCore.QRect(400, 300, 600, 65))
        self.comment.setText("")
        self.comment.setObjectName("comment")
        self.comment.setWordWrap(True)
        self.scrollArea.setWidget(self.comment)

        self.B_A_2 = QtWidgets.QLabel(self.centralwidget)
        self.B_A_2.setGeometry(QtCore.QRect(530, 185, 125, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_A_2.setFont(font)
        self.B_A_2.setStyleSheet("QLabel{background-color: white;}")
        self.B_A_2.setTextFormat(QtCore.Qt.AutoText)
        self.B_A_2.setAlignment(QtCore.Qt.AlignCenter)
        self.B_A_2.setObjectName("B_A_2")

        self.B_A_3 = QtWidgets.QLabel(self.centralwidget)
        self.B_A_3.setGeometry(QtCore.QRect(690, 185, 125, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_A_3.setFont(font)
        self.B_A_3.setStyleSheet("QLabel{background-color: white;}")
        self.B_A_3.setTextFormat(QtCore.Qt.AutoText)
        self.B_A_3.setAlignment(QtCore.Qt.AlignCenter)
        self.B_A_3.setObjectName("B_A_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.radioB.setChecked(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVOL"))
        self.label_2.setText(_translate("MainWindow", "Длина ( В )"))
        self.label_3.setText(_translate("MainWindow", "Ширина ( А )"))
        self.label_4.setText(_translate("MainWindow", "Высота ( С )"))
        self.label_5.setText(_translate("MainWindow", "Профиль"))
        self.radioB.setText(_translate("MainWindow", "B / C"))
        self.radioE.setText(_translate("MainWindow", "E"))
        self.radioEB.setText(_translate("MainWindow", "EB"))
        self.radioBC.setText(_translate("MainWindow", "BC"))
        self.Button.setText(_translate("MainWindow", "Расчет"))
        self.A1.setText(_translate("MainWindow", "<html><head/><body><p>A1</p></body></html>"))
        self.B1.setText(_translate("MainWindow",
                                   "<html><head/><body><p><span style=\" color:#black;\">B1</span></p></body></html>"))
        self.A2.setText(_translate("MainWindow",
                                   "<html><head/><body><p><span style=\" color:#black;\">А2</span></p></body></html>"))
        self.B2.setText(_translate("MainWindow",
                                   "<html><head/><body><p><span style=\" color:#black;\">B2</span></p></body></html>"))
        self.L.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" color:#black;\">L</span></p></body></html>"))
        self.K.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" color:#black;\">K</span></p></body></html>"))
        self.C.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" color:#black;\">C</span></p></body></html>"))
        self.W.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" color:#black;\">W</span></p></body></html>"))
        self.BplusA.setText(_translate("MainWindow", "<html><head/><body><p>B1+A2</p></body></html>"))
        self.B_A.setText(_translate("MainWindow", "<html><head/><body><p>B/A</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "комментарий"))
        self.B_A_2.setText(_translate("MainWindow", "<html><head/><body><p>C/B</p></body></html>"))
        self.B_A_3.setText(_translate("MainWindow", "<html><head/><body><p>C/A</p></body></html>"))

    def calculation(self):

        ls_comment = []
        try:
            length = int(self.inputB.text())
            if length == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('Нужно ввести значение длины')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле длины. Перезапуск программы')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)
        try:
            width = int(self.inputA.text())
            if width == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('Нужно ввести значение ширины')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле ширины. Перезапуск программы')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)
        try:
            heigth = int(self.inputC.text())
            if heigth == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('Нужно ввести значение высоты')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле высоты. Перезапуск программы')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)


        if self.radioB.isChecked():
            A1 = width + 2
            A2 = width + 4
            B1 = length + 4
            B2 = length + 2
            C = heigth + 4

            if length > width:
                K = math.floor((width + 2) / 2)
            else:
                K = math.floor((length + 2) / 2)

            W = K * 2 + C
            L = A1 + A2 + B1 + B2 + 35
            BplusA = B1 + A2
            B_A = round((B2 / A2), 2)
            B_A_2 = round((C / B2), 2)
            B_A_3 = round((C / A2), 2)
        elif self.radioE.isChecked():
            A1 = width + 1
            A2 = width + 2
            B1 = length + 2
            B2 = length + 1
            C = heigth + 2

            if length > width:
                K = math.floor((width + 1) / 2)
            else:
                K = math.floor((length + 1) / 2)

            W = K * 2 + C
            L = A1 + A2 + B1 + B2 + 35
            BplusA = B1 + A2
            B_A = round((B2 / A2), 2)
            B_A_2 = round((C / B2), 2)
            B_A_3 = round((C / A2), 2)
        elif self.radioEB.isChecked():
            A1 = width + 5
            A2 = width + 5
            B1 = length + 5
            B2 = length + 3
            C = heigth + 10

            if length > width:
                K = math.floor((width + 5) / 2)
            else:
                K = math.floor((length + 5) / 2)

            W = K * 2 + C
            L = A1 + A2 + B1 + B2 + 40
            BplusA = B1 + A2
            B_A = round((B2 / A2), 2)
            B_A_2 = round((C / B2), 2)
            B_A_3 = round((C / A2), 2)
        elif self.radioBC.isChecked():
            A1 = width + 8
            A2 = width + 8
            B1 = length + 8
            B2 = length + 4
            C = heigth + 14

            if length > width:
                K = math.floor((width + 8) / 2)
            else:
                K = math.floor((length + 8) / 2)

            W = K * 2 + C
            L = A1 + A2 + B1 + B2 + 40
            BplusA = B1 + A2
            B_A = round((B2 / A2), 2)
            B_A_2 = round((C / B2), 2)
            B_A_3 = round((C / A2), 2)

        if A1 > 185 and A1 < 955:
            self.A1.setText("{}".format(A1))
            self.A1.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.A1.setText("{}".format(A1))
            self.A1.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер ширины (min 185, max 955)')
        if A2 > 185 and A2 < 955:
            self.A2.setText("{}".format(A2))
            self.A2.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.A2.setText("{}".format(A2))
            self.A2.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер ширины (min 185, max 955)')

        if B1 > 90 and B1 < 785:
            self.B1.setText("{}".format(B1))
            self.B1.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.B1.setText("{}".format(B1))
            self.B1.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер длины (min 90, max 785)')
        if B2 > 85 and B2 < 785:
            self.B2.setText("{}".format(B2))
            self.B2.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.B2.setText("{}".format(B2))
            self.B2.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер длины (min 90, max 785)')

        if C > 60 and C < 498:
            self.C.setText("{}".format(C))
            self.C.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.C.setText("{}".format(C))
            self.C.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер высоты (min 60, max 498)')

        if K > 0 and K < 280:
            self.K.setText("{}".format(K))
            self.K.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.K.setText("{}".format(K))
            self.K.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер клапана (мах 280)')

        if W > 250 and W < 1220:
            self.W.setText("{}".format(W))
            self.W.setStyleSheet("""background-color: white; color: green;""")
            if W > 950:
                ls_comment.append('режим скипфид (>950)')
        else:
            self.W.setText("{}".format(W))
            self.W.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер ширины заготовки (min 250, max 1220)')

        if L > 690 and L < 2545:
            self.L.setText("{}".format(L))
            self.L.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.L.setText("{}".format(L))
            self.L.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимый размер длины заготовки (min 690, max 2545)')

        if BplusA > 330 and BplusA < 1250:
            self.BplusA.setText("B+A={}".format(BplusA))
            self.BplusA.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.BplusA.setText("B+A={}".format(BplusA))
            self.BplusA.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимая сумма ширины и длины (min 330, max 1250)')

        if B_A > 0.25 and B_A < 4.0:
            self.B_A.setText("B/A={}".format(B_A))
            self.B_A.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.B_A.setText("B/A={}".format(B_A))
            self.B_A.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимое отношение длины к ширине (min 0.25, max 4)')

        if B_A_2 > 0.25 and B_A_2 < 3.0:
            self.B_A_2.setText("С/В={}".format(B_A_2))
            self.B_A_2.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.B_A_2.setText("С/В={}".format(B_A_2))
            self.B_A_2.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимое отношение высоты к длине (min 0.25, max 3)')

        if B_A_3 > 0.25 and B_A_3 < 3.0:
            self.B_A_3.setText("С/А={}".format(B_A_3))
            self.B_A_3.setStyleSheet("""background-color: white; color: green;""")
        else:
            self.B_A_3.setText("С/А={}".format(B_A_3))
            self.B_A_3.setStyleSheet("""background-color: white; color: red;""")
            ls_comment.append('Не допустимое отношение высоты к ширине (min 0.25, max 3)')

        ls_comment = set(ls_comment)
        text = ''
        for line in ls_comment:
            text = text + line + '\n'
        self.comment.setText("{}".format(text))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comment.setFont(font)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
