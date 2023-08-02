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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1421, 930)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # -------------------pict------------------------------------------------------
        self.Y_W = QtWidgets.QLabel(self.centralwidget)
        self.Y_W.setGeometry(QtCore.QRect(390, 20, 1000, 405))
        self.Y_W.setText("")
        self.Y_W.setPixmap(QtGui.QPixmap("img/Y_W.png"))
        self.Y_W.setScaledContents(True)
        self.Y_W.setObjectName("Y_W")

        self.Y_L = QtWidgets.QLabel(self.centralwidget)
        self.Y_L.setGeometry(QtCore.QRect(390, 500, 1000, 405))
        self.Y_L.setText("")
        self.Y_L.setPixmap(QtGui.QPixmap("img/Y_L.png"))
        self.Y_L.setScaledContents(True)
        self.Y_L.setObjectName("Y_L")

        rx = QtCore.QRegExp("[0-9]{4}")
        val = QtGui.QRegExpValidator(rx)
        # -------------------------input--------------------------------------
        self.length_txt = QtWidgets.QLabel(self.centralwidget)
        self.length_txt.setGeometry(QtCore.QRect(30, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.length_txt.setFont(font)
        self.length_txt.setObjectName("length_txt")

        self.width_txt = QtWidgets.QLabel(self.centralwidget)
        self.width_txt.setGeometry(QtCore.QRect(30, 120, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.width_txt.setFont(font)
        self.width_txt.setObjectName("width_txt")

        self.height_txt = QtWidgets.QLabel(self.centralwidget)
        self.height_txt.setGeometry(QtCore.QRect(30, 180, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.height_txt.setFont(font)
        self.height_txt.setObjectName("height_txt")

        self.length_inp = ClickableLineEdit(self.centralwidget)
        self.length_inp.setGeometry(QtCore.QRect(240, 60, 104, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.length_inp.setFont(font)
        self.length_inp.setObjectName("length_inp")
        self.length_inp.setValidator(val)
        self.length_inp.clicked.connect(self.length_inp.clear)

        self.width_inp = ClickableLineEdit(self.centralwidget)
        self.width_inp.setGeometry(QtCore.QRect(240, 120, 104, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.width_inp.setFont(font)
        self.width_inp.setObjectName("width_inp")
        self.width_inp.setValidator(val)
        self.width_inp.clicked.connect(self.width_inp.clear)

        self.height_inp = ClickableLineEdit(self.centralwidget)
        self.height_inp.setGeometry(QtCore.QRect(240, 180, 104, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.height_inp.setFont(font)
        self.height_inp.setObjectName("height_inp")
        self.height_inp.setValidator(val)
        self.height_inp.clicked.connect(self.height_inp.clear)
        # -------------------------------radio-------------------------------------------------------
        self.radio_B = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_B.setGeometry(QtCore.QRect(30, 290, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_B.sizePolicy().hasHeightForWidth())
        self.radio_B.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.radio_B.setFont(font)
        self.radio_B.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radio_B.setTabletTracking(True)
        self.radio_B.setAutoFillBackground(False)
        self.radio_B.setIconSize(QtCore.QSize(20, 20))
        self.radio_B.setChecked(False)
        self.radio_B.setObjectName("radio_B")

        self.radio_E = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_E.setGeometry(QtCore.QRect(30, 360, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_E.sizePolicy().hasHeightForWidth())
        self.radio_E.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.radio_E.setFont(font)
        self.radio_E.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radio_E.setTabletTracking(True)
        self.radio_E.setAutoFillBackground(False)
        self.radio_E.setIconSize(QtCore.QSize(20, 20))
        self.radio_E.setChecked(False)
        self.radio_E.setObjectName("radio_E")

        self.radio_BC = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_BC.setGeometry(QtCore.QRect(200, 360, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_BC.sizePolicy().hasHeightForWidth())
        self.radio_BC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.radio_BC.setFont(font)
        self.radio_BC.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radio_BC.setTabletTracking(True)
        self.radio_BC.setAutoFillBackground(False)
        self.radio_BC.setIconSize(QtCore.QSize(20, 20))
        self.radio_BC.setChecked(False)
        self.radio_BC.setObjectName("radio_BC")

        self.radio_EB = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_EB.setGeometry(QtCore.QRect(200, 290, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_EB.sizePolicy().hasHeightForWidth())
        self.radio_EB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.radio_EB.setFont(font)
        self.radio_EB.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radio_EB.setTabletTracking(True)
        self.radio_EB.setAutoFillBackground(False)
        self.radio_EB.setIconSize(QtCore.QSize(20, 20))
        self.radio_EB.setChecked(False)
        self.radio_EB.setObjectName("radio_EB")
        # ---------------------------------info_line-----------------------------------------------
        self.info_line_txt = QtWidgets.QLabel(self.centralwidget)
        self.info_line_txt.setGeometry(QtCore.QRect(20, 500, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.info_line_txt.setFont(font)
        self.info_line_txt.setScaledContents(True)
        self.info_line_txt.setObjectName("info_line_txt")

        self.line_EVOL = QtWidgets.QLabel(self.centralwidget)
        self.line_EVOL.setGeometry(QtCore.QRect(720, 240, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_EVOL.setFont(font)
        self.line_EVOL.setObjectName("line_EVOL")

        self.line_EVOL_2 = QtWidgets.QLabel(self.centralwidget)
        self.line_EVOL_2.setGeometry(QtCore.QRect(1010, 720, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_EVOL_2.setFont(font)
        self.line_EVOL_2.setObjectName("line_EVOL_2")

        self.line_618 = QtWidgets.QLabel(self.centralwidget)
        self.line_618.setGeometry(QtCore.QRect(20, 550, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_618.setFont(font)
        self.line_618.setObjectName("line_618")

        self.line_924 = QtWidgets.QLabel(self.centralwidget)
        self.line_924.setGeometry(QtCore.QRect(20, 600, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_924.setFont(font)
        self.line_924.setObjectName("line_924")

        self.line_1228 = QtWidgets.QLabel(self.centralwidget)
        self.line_1228.setGeometry(QtCore.QRect(20, 650, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_1228.setFont(font)
        self.line_1228.setObjectName("line_1228")

        self.line_bobst = QtWidgets.QLabel(self.centralwidget)
        self.line_bobst.setGeometry(QtCore.QRect(20, 720, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.line_bobst.setFont(font)
        self.line_bobst.setObjectName("line_bobst")

        self.square_m2 = QtWidgets.QLabel(self.centralwidget)
        self.square_m2.setGeometry(QtCore.QRect(20, 430, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.square_m2.setFont(font)
        self.square_m2.setScaledContents(True)
        self.square_m2.setObjectName("square_m2")
        # ---------------------------output Y_W-------------------------------------------------------
        self.YW_w1 = QtWidgets.QLabel(self.centralwidget)
        self.YW_w1.setGeometry(QtCore.QRect(540, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_w1.setFont(font)
        self.YW_w1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_w1.setAutoFillBackground(False)
        self.YW_w1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_w1.setScaledContents(True)
        self.YW_w1.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_w1.setObjectName("YW_w1")

        self.YW_l1 = QtWidgets.QLabel(self.centralwidget)
        self.YW_l1.setGeometry(QtCore.QRect(760, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_l1.setFont(font)
        self.YW_l1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_l1.setAutoFillBackground(False)
        self.YW_l1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_l1.setScaledContents(True)
        self.YW_l1.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_l1.setObjectName("YW_l1")

        self.YW_w2 = QtWidgets.QLabel(self.centralwidget)
        self.YW_w2.setGeometry(QtCore.QRect(980, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_w2.setFont(font)
        self.YW_w2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_w2.setAutoFillBackground(False)
        self.YW_w2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_w2.setScaledContents(True)
        self.YW_w2.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_w2.setObjectName("YW_w2")

        self.YW_l2 = QtWidgets.QLabel(self.centralwidget)
        self.YW_l2.setGeometry(QtCore.QRect(1210, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_l2.setFont(font)
        self.YW_l2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_l2.setAutoFillBackground(False)
        self.YW_l2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_l2.setScaledContents(True)
        self.YW_l2.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_l2.setObjectName("YW_l2")

        self.YW_work_H = QtWidgets.QLabel(self.centralwidget)
        self.YW_work_H.setGeometry(QtCore.QRect(370, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_work_H.setFont(font)
        self.YW_work_H.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_work_H.setAutoFillBackground(False)
        self.YW_work_H.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_work_H.setScaledContents(True)
        self.YW_work_H.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_work_H.setObjectName("YW_work_H")

        self.YW_k = QtWidgets.QLabel(self.centralwidget)
        self.YW_k.setGeometry(QtCore.QRect(430, 360, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_k.setFont(font)
        self.YW_k.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_k.setAutoFillBackground(False)
        self.YW_k.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_k.setScaledContents(True)
        self.YW_k.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_k.setObjectName("YW_k")

        self.YW_h = QtWidgets.QLabel(self.centralwidget)
        self.YW_h.setGeometry(QtCore.QRect(430, 250, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_h.setFont(font)
        self.YW_h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_h.setAutoFillBackground(False)
        self.YW_h.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_h.setScaledContents(True)
        self.YW_h.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_h.setObjectName("YW_h")

        self.YW_work_l = QtWidgets.QLabel(self.centralwidget)
        self.YW_work_l.setGeometry(QtCore.QRect(880, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YW_work_l.setFont(font)
        self.YW_work_l.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YW_work_l.setAutoFillBackground(False)
        self.YW_work_l.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YW_work_l.setScaledContents(True)
        self.YW_work_l.setAlignment(QtCore.Qt.AlignCenter)
        self.YW_work_l.setObjectName("YW_work_l")
        # _____________________________output Y_L___________________________________________________________
        self.YL_l2 = QtWidgets.QLabel(self.centralwidget)
        self.YL_l2.setGeometry(QtCore.QRect(600, 550, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_l2.setFont(font)
        self.YL_l2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_l2.setAutoFillBackground(False)
        self.YL_l2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_l2.setScaledContents(True)
        self.YL_l2.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_l2.setObjectName("YL_l2")

        self.YL_work_H = QtWidgets.QLabel(self.centralwidget)
        self.YL_work_H.setGeometry(QtCore.QRect(370, 660, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_work_H.setFont(font)
        self.YL_work_H.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_work_H.setAutoFillBackground(False)
        self.YL_work_H.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_work_H.setScaledContents(True)
        self.YL_work_H.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_work_H.setObjectName("YL_work_H")

        self.YL_h = QtWidgets.QLabel(self.centralwidget)
        self.YL_h.setGeometry(QtCore.QRect(430, 720, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_h.setFont(font)
        self.YL_h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_h.setAutoFillBackground(False)
        self.YL_h.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_h.setScaledContents(True)
        self.YL_h.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_h.setObjectName("YL_h")

        self.YL_work_L = QtWidgets.QLabel(self.centralwidget)
        self.YL_work_L.setGeometry(QtCore.QRect(900, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_work_L.setFont(font)
        self.YL_work_L.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_work_L.setAutoFillBackground(False)
        self.YL_work_L.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_work_L.setScaledContents(True)
        self.YL_work_L.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_work_L.setObjectName("YL_work_L")

        self.YL_w2 = QtWidgets.QLabel(self.centralwidget)
        self.YL_w2.setGeometry(QtCore.QRect(830, 550, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_w2.setFont(font)
        self.YL_w2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_w2.setAutoFillBackground(False)
        self.YL_w2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_w2.setScaledContents(True)
        self.YL_w2.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_w2.setObjectName("YL_w2")

        self.YL_k = QtWidgets.QLabel(self.centralwidget)
        self.YL_k.setGeometry(QtCore.QRect(430, 840, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_k.setFont(font)
        self.YL_k.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_k.setAutoFillBackground(False)
        self.YL_k.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_k.setScaledContents(True)
        self.YL_k.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_k.setObjectName("YL_k")

        self.YL_l1 = QtWidgets.QLabel(self.centralwidget)
        self.YL_l1.setGeometry(QtCore.QRect(1050, 550, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_l1.setFont(font)
        self.YL_l1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_l1.setAutoFillBackground(False)
        self.YL_l1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_l1.setScaledContents(True)
        self.YL_l1.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_l1.setObjectName("YL_l1")

        self.YL_w1 = QtWidgets.QLabel(self.centralwidget)
        self.YL_w1.setGeometry(QtCore.QRect(1270, 550, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.YL_w1.setFont(font)
        self.YL_w1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.YL_w1.setAutoFillBackground(False)
        self.YL_w1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.YL_w1.setScaledContents(True)
        self.YL_w1.setAlignment(QtCore.Qt.AlignCenter)
        self.YL_w1.setObjectName("YL_w1")
        # ----------------------output koef-------------------------------------------
        self.L_div_W = QtWidgets.QLabel(self.centralwidget)
        self.L_div_W.setGeometry(QtCore.QRect(1125, 360, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.L_div_W.setFont(font)
        self.L_div_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_div_W.setAutoFillBackground(False)
        self.L_div_W.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_div_W.setScaledContents(True)
        self.L_div_W.setAlignment(QtCore.Qt.AlignCenter)
        self.L_div_W.setObjectName("L_div_W")

        self.L_L_div_W = QtWidgets.QLabel(self.centralwidget)
        self.L_L_div_W.setGeometry(QtCore.QRect(980, 620, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.L_L_div_W.setFont(font)
        self.L_L_div_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_L_div_W.setAutoFillBackground(False)
        self.L_L_div_W.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_L_div_W.setScaledContents(True)
        self.L_L_div_W.setAlignment(QtCore.Qt.AlignCenter)
        self.L_L_div_W.setObjectName("L_L_div_W")

        self.H_div_L = QtWidgets.QLabel(self.centralwidget)
        self.H_div_L.setGeometry(QtCore.QRect(720, 450, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.H_div_L.setFont(font)
        self.H_div_L.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.H_div_L.setAutoFillBackground(False)
        self.H_div_L.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.H_div_L.setScaledContents(True)
        self.H_div_L.setAlignment(QtCore.Qt.AlignCenter)
        self.H_div_L.setObjectName("H_div_L")

        self.H_div_W = QtWidgets.QLabel(self.centralwidget)
        self.H_div_W.setGeometry(QtCore.QRect(950, 450, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.H_div_W.setFont(font)
        self.H_div_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.H_div_W.setAutoFillBackground(False)
        self.H_div_W.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.H_div_W.setScaledContents(True)
        self.H_div_W.setAlignment(QtCore.Qt.AlignCenter)
        self.H_div_W.setObjectName("H_div_W")

        self.L_plus_W = QtWidgets.QLabel(self.centralwidget)
        self.L_plus_W.setGeometry(QtCore.QRect(440, 450, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.L_plus_W.setFont(font)
        self.L_plus_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.L_plus_W.setAutoFillBackground(False)
        self.L_plus_W.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_plus_W.setScaledContents(True)
        self.L_plus_W.setAlignment(QtCore.Qt.AlignCenter)
        self.L_plus_W.setObjectName("L_plus_W")

        # ------------------------------button------------------------------
        self.Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.calculation())
        self.Button.setGeometry(QtCore.QRect(40, 810, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.Button.setFont(font)
        self.Button.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.Button.setObjectName("Button")

        # ------------------------------ERROR_YW------------------------------
        self.error_w1 = QtWidgets.QLabel(self.centralwidget)
        self.error_w1.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_w1.setFont(font)
        self.error_w1.setObjectName("error_w1")

        self.error_w2 = QtWidgets.QLabel(self.centralwidget)
        self.error_w2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_w2.setFont(font)
        self.error_w2.setObjectName("error_w2")

        self.error_l1 = QtWidgets.QLabel(self.centralwidget)
        self.error_l1.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_l1.setFont(font)
        self.error_l1.setObjectName("error_l1")

        self.error_l2 = QtWidgets.QLabel(self.centralwidget)
        self.error_l2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_l2.setFont(font)
        self.error_l2.setObjectName("error_l2")

        self.error_h = QtWidgets.QLabel(self.centralwidget)
        self.error_h.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_h.setFont(font)
        self.error_h.setObjectName("error_h")

        self.error_k = QtWidgets.QLabel(self.centralwidget)
        self.error_k.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_k.setFont(font)
        self.error_k.setObjectName("error_k")

        self.error_WL = QtWidgets.QLabel(self.centralwidget)
        self.error_WL.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_WL.setFont(font)
        self.error_WL.setObjectName("error_WL")

        self.error_WH = QtWidgets.QLabel(self.centralwidget)
        self.error_WH.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_WH.setFont(font)
        self.error_WH.setObjectName("error_WH")

        # ------------------------------ERROR_YL------------------------------
        self.error_lw1 = QtWidgets.QLabel(self.centralwidget)
        self.error_lw1.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lw1.setFont(font)
        self.error_lw1.setObjectName("error_lw1")

        self.error_lw2 = QtWidgets.QLabel(self.centralwidget)
        self.error_lw2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lw2.setFont(font)
        self.error_lw2.setObjectName("error_lw2")

        self.error_ll1 = QtWidgets.QLabel(self.centralwidget)
        self.error_ll1.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_ll1.setFont(font)
        self.error_ll1.setObjectName("error_ll1")

        self.error_ll2 = QtWidgets.QLabel(self.centralwidget)
        self.error_ll2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_ll2.setFont(font)
        self.error_ll2.setObjectName("error_ll2")

        self.error_lh = QtWidgets.QLabel(self.centralwidget)
        self.error_lh.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lh.setFont(font)
        self.error_lh.setObjectName("error_lh")

        self.error_lk = QtWidgets.QLabel(self.centralwidget)
        self.error_lk.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lk.setFont(font)
        self.error_lk.setObjectName("error_lk")

        self.error_lWL = QtWidgets.QLabel(self.centralwidget)
        self.error_lWL.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lWL.setFont(font)
        self.error_lWL.setObjectName("error_lWL")

        self.error_lWH = QtWidgets.QLabel(self.centralwidget)
        self.error_lWH.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_lWH.setFont(font)
        self.error_lWH.setObjectName("error_lWH")

        self.error_sq_1228 = QtWidgets.QLabel(self.centralwidget)
        self.error_sq_1228.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.error_sq_1228.setFont(font)
        self.error_sq_1228.setObjectName("error_sq_1228")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.length_txt.setText(_translate("MainWindow", "Длина (L)"))
        self.width_txt.setText(_translate("MainWindow", "Ширина (W)"))
        self.height_txt.setText(_translate("MainWindow", "Высота (H)"))
        self.radio_B.setText(_translate("MainWindow", "B(C)"))
        self.radio_E.setText(_translate("MainWindow", "E"))
        self.radio_BC.setText(_translate("MainWindow", "BC"))
        self.radio_EB.setText(_translate("MainWindow", "EB"))
        self.info_line_txt.setText(_translate("MainWindow", "Возможные линии изготовления"))
        self.line_EVOL.setText(_translate("MainWindow", "EVOL-100"))
        self.line_618.setText(_translate("MainWindow", "FFG-618"))
        self.line_924.setText(_translate("MainWindow", "FFG-924"))
        self.line_1228.setText(_translate("MainWindow", "FFG-1228"))
        self.line_bobst.setText(_translate("MainWindow", "только штампом"))
        self.square_m2.setText(_translate("MainWindow", "Площадь "))
        self.YW_w1.setText(_translate("MainWindow", "W1"))
        self.YW_l1.setText(_translate("MainWindow", "L1"))
        self.YW_w2.setText(_translate("MainWindow", "W2"))
        self.YW_l2.setText(_translate("MainWindow", "L2"))
        self.YW_work_H.setText(_translate("MainWindow", "work_H"))
        self.YW_k.setText(_translate("MainWindow", "K"))
        self.YW_h.setText(_translate("MainWindow", "H"))
        self.L_plus_W.setText(_translate("MainWindow", "L + W"))
        self.L_L_div_W.setText(_translate("MainWindow", "W2 / L2"))
        self.YL_l2.setText(_translate("MainWindow", "L2"))
        self.YL_work_H.setText(_translate("MainWindow", "work_H"))
        self.YL_h.setText(_translate("MainWindow", "H"))
        self.YL_work_L.setText(_translate("MainWindow", "work_L"))
        self.YL_w2.setText(_translate("MainWindow", "W2"))
        self.YL_k.setText(_translate("MainWindow", "K"))
        self.YL_l1.setText(_translate("MainWindow", "L1"))
        self.YL_w1.setText(_translate("MainWindow", "W1"))
        self.L_div_W.setText(_translate("MainWindow", "L1 / W1"))
        self.H_div_L.setText(_translate("MainWindow", "H / L"))
        self.H_div_W.setText(_translate("MainWindow", "H / W"))
        self.YW_work_l.setText(_translate("MainWindow", "work_L"))
        self.line_EVOL_2.setText(_translate("MainWindow", "EVOL-100"))
        self.Button.setText(_translate("MainWindow", "Расчет"))

    def calculation(self):
        flag_evol = True
        flag_evol_L = True
        flag_618 = True
        flag_924 = True
        flag_1228 = True
        flag_bobst = False

        try:
            length = int(self.length_inp.text())
            if length == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('значение длины не может быть 0')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле длины')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)
        try:
            width = int(self.width_inp.text())
            if width == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('значение ширины не может быть 0')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле ширины')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)
        try:
            heigth = int(self.height_inp.text())
            if heigth == 0:
                err = QMessageBox()
                err.setWindowTitle('Ошибка')
                err.setText('значение высоты не может быть 0')
                err.exec_()
        except Exception as e:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('ПУСТОЕ поле высоты')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)

        if self.radio_B.isChecked():
            w1 = width + 2
            w2 = width + 4
            l1 = length + 4
            l2 = length + 2
            h = heigth + 4
            YL_l2 = l2
            YL_w2 = w2
            YL_w1 = w1
            YL_l1 = l1
            k = math.floor((width + 2) / 2)
            W = k * 2 + h
            L = l1 + l2 + w1 + w2 + 35
            L_plus_W = l1 + w2
            H_div_L = round((heigth / length), 2)
            H_div_W = round((heigth / width), 2)
            L1_div_W1 = round((l1 / w1), 2)
            W2_div_L2 = round((YL_w2 / YL_l2), 2)
            S = round((L * W) / 1000000, 4)
        elif self.radio_E.isChecked():
            w1 = width + 1
            w2 = width + 2
            l1 = length + 2
            l2 = length + 1
            h = heigth + 2
            YL_l2 = l2
            YL_w2 = w2
            YL_w1 = w1
            YL_l1 = l1
            k = math.floor((width + 2) / 2)
            W = k * 2 + h
            L = l1 + l2 + w1 + w2 + 35
            L_plus_W = l1 + w2
            H_div_L = round((heigth / length), 2)
            H_div_W = round((heigth / width), 2)
            L1_div_W1 = round((l1 / w1), 2)
            W2_div_L2 = round((YL_w2 / YL_l2), 2)
            S = round((L * W) / 1000000, 4)

        elif self.radio_EB.isChecked():
            w1 = width + 5
            w2 = width + 5
            l1 = length + 5
            l2 = length + 3
            YL_l2 = length + 5
            YL_w2 = width + 5
            YL_w1 = width + 3
            YL_l1 = length + 5
            h = heigth + 10
            k = math.floor((width + 5) / 2)
            W = k * 2 + h
            L = l1 + l2 + w1 + w2 + 40
            L_plus_W = l1 + w2
            H_div_L = round((heigth / length), 2)
            H_div_W = round((heigth / width), 2)
            L1_div_W1 = round((l1 / w1), 2)
            W2_div_L2 = round((YL_w2 / YL_l2), 2)
            S = round((L * W) / 1000000, 4)

        elif self.radio_BC.isChecked():
            w1 = width + 8
            w2 = width + 8
            l1 = length + 8
            l2 = length + 4
            YL_l2 = length + 8
            YL_w2 = width + 8
            YL_w1 = width + 4
            YL_l1 = length + 8
            h = heigth + 14
            k = math.floor((width + 8) / 2)
            W = k * 2 + h
            L = l1 + l2 + w1 + w2 + 40
            L_plus_W = l1 + w2
            H_div_L = round((heigth / length), 2)
            H_div_W = round((heigth / width), 2)
            L1_div_W1 = round((l1 / w1), 2)
            W2_div_L2 = round((YL_w2 / YL_l2), 2)
            S = round((L * W) / 1000000, 4)

        else:
            err = QMessageBox()
            err.setWindowTitle('Ошибка')
            err.setText('Не выбран профиль')
            err.exec_()
            python = sys.executable
            os.execl(python, python, *sys.argv)

        sq = 'Площадь ' + str(S) + ' m2'
        self.square_m2.setText("{}".format(sq))
        self.square_m2.setStyleSheet(""" color: green;""")

        if S < 0.2:
            flag_evol = False
            flag_924 = False
            flag_1228 = False
            flag_618 = False
            flag_evol_L = False
            flag_bobst = True
            self.square_m2.setText("{}".format(sq))
            self.square_m2.setStyleSheet(""" color: red;""")

        # FOR__EVOL_W
        if w1 > 184 and w1 < 956:
            self.YW_w1.setText("{}".format(w1))
            self.YW_w1.setStyleSheet("""background-color: white; color: green;""")
            self.error_w1.setStyleSheet("""background-color: none;""")
            self.error_w1.clear()
        else:
            if w1 < 185:
                flag_evol = False
                self.YW_w1.setText("{}".format(w1))
                self.YW_w1.setStyleSheet("""background-color: white; color: red;""")
                self.error_w1.setGeometry(QtCore.QRect(540, 100, 81, 41))
                self.error_w1.setText("{}".format('(min 185)'))
                self.error_w1.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_w1.setText("{}".format(w1))
                self.YW_w1.setStyleSheet("""background-color: white; color: red;""")
                self.error_w1.setGeometry(QtCore.QRect(540, 100, 81, 41))
                self.error_w1.setText("{}".format('(max 955)'))
                self.error_w1.setStyleSheet("""background-color: white; color: red;""")

        if w2 > 184 and w2 < 956:
            self.YW_w2.setText("{}".format(w2))
            self.YW_w2.setStyleSheet("""background-color: white; color: green;""")
            self.error_w2.setStyleSheet("""background-color: none;""")
            self.error_w2.clear()
        else:
            if w2 < 185:
                flag_evol = False
                self.YW_w2.setText("{}".format(w2))
                self.YW_w2.setStyleSheet("""background-color: white; color: red;""")
                self.error_w2.setGeometry(QtCore.QRect(980, 100, 81, 41))
                self.error_w2.setText("{}".format('(min 185)'))
                self.error_w2.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_w2.setText("{}".format(w2))
                self.YW_w2.setStyleSheet("""background-color: white; color: red;""")
                self.error_w2.setGeometry(QtCore.QRect(980, 100, 81, 41))
                self.error_w2.setText("{}".format('(max 955)'))
                self.error_w2.setStyleSheet("""background-color: white; color: red;""")

        if l1 > 89 and l1 < 786:
            self.YW_l1.setText("{}".format(l1))
            self.YW_l1.setStyleSheet("""background-color: white; color: green;""")
            self.error_l1.setStyleSheet("""background-color: none;""")
            self.error_l1.clear()
        else:
            if l1 < 90:
                flag_evol = False
                self.YW_l1.setText("{}".format(l1))
                self.YW_l1.setStyleSheet("""background-color: white; color: red;""")
                self.error_l1.setGeometry(QtCore.QRect(760, 100, 81, 41))
                self.error_l1.setText("{}".format('(min 90)'))
                self.error_l1.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_l1.setText("{}".format(l1))
                self.YW_l1.setStyleSheet("""background-color: white; color: red;""")
                self.error_l1.setGeometry(QtCore.QRect(760, 100, 81, 41))
                self.error_l1.setText("{}".format('(max 785)'))
                self.error_l1.setStyleSheet("""background-color: white; color: red;""")

        if l2 > 84 and l2 < 787:
            self.YW_l2.setText("{}".format(l2))
            self.YW_l2.setStyleSheet("""background-color: white; color: green;""")
            self.error_l2.setStyleSheet("""background-color: none;""")
            self.error_l2.clear()
        else:
            if l2 < 85:
                flag_evol = False
                self.YW_l2.setText("{}".format(l2))
                self.YW_l2.setStyleSheet("""background-color: white; color: red;""")
                self.error_l2.setGeometry(QtCore.QRect(1210, 100, 81, 41))
                self.error_l2.setText("{}".format('(min 85)'))
                self.error_l2.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_l2.setText("{}".format(l2))
                self.YW_l2.setStyleSheet("""background-color: white; color: red;""")
                self.error_l2.setGeometry(QtCore.QRect(1210, 100, 81, 41))
                self.error_l2.setText("{}".format('(max 786)'))
                self.error_l2.setStyleSheet("""background-color: white; color: red;""")

        if h > 59 and h < 499:
            self.YW_h.setText("{}".format(h))
            self.YW_h.setStyleSheet("""background-color: white; color: green;""")
            self.error_h.setStyleSheet("""background-color: none;""")
            self.error_h.clear()
        else:
            if h < 60:
                flag_evol = False
                self.YW_h.setText("{}".format(h))
                self.YW_h.setStyleSheet("""background-color: white; color: red;""")
                self.error_h.setGeometry(QtCore.QRect(500, 250, 81, 41))
                self.error_h.setText("{}".format('(min 60)'))
                self.error_h.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_h.setText("{}".format(h))
                self.YW_h.setStyleSheet("""background-color: white; color: red;""")
                self.error_h.setGeometry(QtCore.QRect(500, 250, 81, 41))
                self.error_h.setText("{}".format('(max 498)'))
                self.error_h.setStyleSheet("""background-color: white; color: red;""")

        if k < 281:
            self.YW_k.setText("{}".format(k))
            self.YW_k.setStyleSheet("""background-color: white; color: green;""")
            self.error_k.setStyleSheet("""background-color: none;""")
            self.error_k.clear()
        else:
            flag_evol = False
            self.YW_k.setText("{}".format(k))
            self.YW_k.setStyleSheet("""background-color: white; color: red;""")
            self.error_k.setGeometry(QtCore.QRect(500, 360, 81, 41))
            self.error_k.setText("{}".format('(max 280)'))
            self.error_k.setStyleSheet("""background-color: white; color: red;""")

        if L > 654 and L < 2535:
            self.YW_work_l.setText("{}".format(L))
            self.YW_work_l.setStyleSheet("""background-color: white; color: green;""")
            self.error_WL.setStyleSheet("""background-color: none;""")
            self.error_WL.clear()
        else:
            if L < 655:
                flag_evol = False
                self.YW_work_l.setText("{}".format(L))
                self.YW_work_l.setStyleSheet("""background-color: white; color: red;""")
                self.error_WL.setGeometry(QtCore.QRect(880, 60, 90, 41))
                self.error_WL.setText("{}".format('(min 655)'))
                self.error_WL.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_work_l.setText("{}".format(L))
                self.YW_work_l.setStyleSheet("""background-color: white; color: red;""")
                self.error_WL.setGeometry(QtCore.QRect(880, 60, 90, 41))
                self.error_WL.setText("{}".format('(max 2500)'))
                self.error_WL.setStyleSheet("""background-color: white; color: red;""")

        if W > 249 and W < 950:
            self.YW_work_H.setText("{}".format(W))
            self.YW_work_H.setStyleSheet("""background-color: white; color: green;""")
            self.error_WH.setStyleSheet("""background-color: none;""")
            self.error_WH.clear()

        else:
            if W < 250:
                flag_evol = False
                self.YW_work_H.setText("{}".format(W))
                self.YW_work_H.setStyleSheet("""background-color: white; color: red;""")
                self.error_WH.setGeometry(QtCore.QRect(380, 210, 90, 41))
                self.error_WH.setText("{}".format('(min 250)'))
                self.error_WH.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol = False
                self.YW_work_H.setText("{}".format(W))
                self.YW_work_H.setStyleSheet("""background-color: white; color: red;""")
                self.error_WH.setGeometry(QtCore.QRect(380, 210, 90, 41))
                self.error_WH.setText("{}".format('(max 950)'))
                self.error_WH.setStyleSheet("""background-color: white; color: red;""")

        # -------------------------------------------- FOR__EVOL_L--------------------------------------------
        if YL_w1 > 84 and YL_w1 < 787:
            self.YL_w1.setText("{}".format(YL_w1))
            self.YL_w1.setStyleSheet("""background-color: white; color: green;""")
            self.error_lw1.setStyleSheet("""background-color: none;""")
            self.error_lw1.clear()
        else:
            if YL_w1 < 85:
                flag_evol_L = False
                self.YL_w1.setText("{}".format(YL_w1))
                self.YL_w1.setStyleSheet("""background-color: white; color: red;""")
                self.error_lw1.setGeometry(QtCore.QRect(1270, 580, 81, 41))
                self.error_lw1.setText("{}".format('(min 85)'))
                self.error_lw1.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_w1.setText("{}".format(YL_w1))
                self.YL_w1.setStyleSheet("""background-color: white; color: red;""")
                self.error_lw1.setGeometry(QtCore.QRect(1270, 580, 81, 41))
                self.error_lw1.setText("{}".format('(max 786)'))
                self.error_lw1.setStyleSheet("""background-color: white; color: red;""")

        if YL_w2 > 89 and YL_w2 < 786:
            self.YL_w2.setText("{}".format(YL_w2))
            self.YL_w2.setStyleSheet("""background-color: white; color: green;""")
            self.error_lw2.setStyleSheet("""background-color: none;""")
            self.error_lw2.clear()
        else:
            if YL_w2 < 90:
                flag_evol_L = False
                self.YL_w2.setText("{}".format(YL_w2))
                self.YL_w2.setStyleSheet("""background-color: white; color: red;""")
                self.error_lw2.setGeometry(QtCore.QRect(830, 580, 81, 41))
                self.error_lw2.setText("{}".format('(min 90)'))
                self.error_lw2.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_w2.setText("{}".format(YL_w2))
                self.YL_w2.setStyleSheet("""background-color: white; color: red;""")
                self.error_lw2.setGeometry(QtCore.QRect(830, 580, 81, 41))
                self.error_lw2.setText("{}".format('(max 785)'))
                self.error_lw2.setStyleSheet("""background-color: white; color: red;""")

        if YL_l1 > 184 and YL_l1 < 956:
            self.YL_l1.setText("{}".format(YL_l1))
            self.YL_l1.setStyleSheet("""background-color: white; color: green;""")
            self.error_ll1.setStyleSheet("""background-color: none;""")
            self.error_ll1.clear()
        else:
            if YL_l1 < 185:
                flag_evol_L = False
                self.YL_l1.setText("{}".format(YL_l1))
                self.YL_l1.setStyleSheet("""background-color: white; color: red;""")
                self.error_ll1.setGeometry(QtCore.QRect(1050, 580, 81, 41))
                self.error_ll1.setText("{}".format('(min 185)'))
                self.error_ll1.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_l1.setText("{}".format(YL_l1))
                self.YL_l1.setStyleSheet("""background-color: white; color: red;""")
                self.error_ll1.setGeometry(QtCore.QRect(1050, 580, 81, 41))
                self.error_ll1.setText("{}".format('(max 955)'))
                self.error_ll1.setStyleSheet("""background-color: white; color: red;""")

        if YL_l2 > 184 and YL_l2 < 956:
            self.YL_l2.setText("{}".format(YL_l2))
            self.YL_l2.setStyleSheet("""background-color: white; color: green;""")
            self.error_ll2.setStyleSheet("""background-color: none;""")
            self.error_ll2.clear()
        else:
            if YL_l2 < 185:
                flag_evol_L = False
                self.YL_l2.setText("{}".format(YL_l2))
                self.YL_l2.setStyleSheet("""background-color: white; color: red;""")
                self.error_ll2.setGeometry(QtCore.QRect(600, 580, 81, 41))
                self.error_ll2.setText("{}".format('(min 185)'))
                self.error_ll2.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_l2.setText("{}".format(YL_l2))
                self.YL_l2.setStyleSheet("""background-color: white; color: red;""")
                self.error_ll2.setGeometry(QtCore.QRect(600, 580, 81, 41))
                self.error_ll2.setText("{}".format('(max 955)'))
                self.error_ll2.setStyleSheet("""background-color: white; color: red;""")

        if h > 59 and h < 499:
            self.YL_h.setText("{}".format(h))
            self.YL_h.setStyleSheet("""background-color: white; color: green;""")
            self.error_lh.setStyleSheet("""background-color: none;""")
            self.error_lh.clear()
        else:
            if h < 60:
                flag_evol_L = False
                self.YL_h.setText("{}".format(h))
                self.YL_h.setStyleSheet("""background-color: white; color: red;""")
                self.error_lh.setGeometry(QtCore.QRect(430, 750, 81, 41))
                self.error_lh.setText("{}".format('(min 60)'))
                self.error_lh.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_h.setText("{}".format(h))
                self.YL_h.setStyleSheet("""background-color: white; color: red;""")
                self.error_lh.setGeometry(QtCore.QRect(430, 750, 81, 41))
                self.error_lh.setText("{}".format('(max 498)'))
                self.error_lh.setStyleSheet("""background-color: white; color: red;""")

        if k < 281:
            self.YL_k.setText("{}".format(k))
            self.YL_k.setStyleSheet("""background-color: white; color: green;""")
            self.error_lk.setStyleSheet("""background-color: none;""")
            self.error_lk.clear()
        else:
            flag_evol_L = False
            self.YL_k.setText("{}".format(k))
            self.YL_k.setStyleSheet("""background-color: white; color: red;""")
            self.error_lk.setGeometry(QtCore.QRect(430, 870, 81, 41))
            self.error_lk.setText("{}".format('(max 280)'))
            self.error_lk.setStyleSheet("""background-color: white; color: red;""")

        if L > 654 and L < 2535:
            self.YL_work_L.setText("{}".format(L))
            self.YL_work_L.setStyleSheet("""background-color: white; color: green;""")
            self.error_lWL.setStyleSheet("""background-color: none;""")
            self.error_lWL.clear()
        else:
            if L < 655:
                flag_evol_L = False
                self.YL_work_L.setText("{}".format(L))
                self.YL_work_L.setStyleSheet("""background-color: white; color: red;""")
                self.error_lWL.setGeometry(QtCore.QRect(900, 540, 90, 41))
                self.error_lWL.setText("{}".format('(min 655)'))
                self.error_lWL.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_work_L.setText("{}".format(L))
                self.YL_work_L.setStyleSheet("""background-color: white; color: red;""")
                self.error_lWL.setGeometry(QtCore.QRect(900, 540, 90, 41))
                self.error_lWL.setText("{}".format('(max 2500)'))
                self.error_lWL.setStyleSheet("""background-color: white; color: red;""")

        if W > 249 and W < 951:
            self.YL_work_H.setText("{}".format(W))
            self.YL_work_H.setStyleSheet("""background-color: white; color: green;""")
            self.error_lWH.setStyleSheet("""background-color: none;""")
            self.error_lWH.clear()
        else:
            if W < 250:
                flag_evol_L = False
                self.YL_work_H.setText("{}".format(W))
                self.YL_work_H.setStyleSheet("""background-color: white; color: red;""")
                self.error_lWH.setGeometry(QtCore.QRect(370, 690, 90, 41))
                self.error_lWH.setText("{}".format('(min 250)'))
                self.error_lWH.setStyleSheet("""background-color: white; color: red;""")
            else:
                flag_evol_L = False
                self.YL_work_H.setText("{}".format(W))
                self.YL_work_H.setStyleSheet("""background-color: white; color: red;""")
                self.error_lWH.setGeometry(QtCore.QRect(370, 690, 90, 41))
                self.error_lWH.setText("{}".format('(max 950)'))
                self.error_lWH.setStyleSheet("""background-color: white; color: red;""")

        # -------------------------------------------- koef--------------------------------------------
        if L_plus_W > 329 and L_plus_W < 1251:
            out = 'L+W= ' + str(L_plus_W)
            self.L_plus_W.setText("{}".format(out))
            self.L_plus_W.setStyleSheet("""background-color: white; color: green;""")
        else:
            if L_plus_W < 250:
                flag_evol = False
                flag_evol_L = False
                out = 'L+W= ' + str(L_plus_W) + ' (min 330)'
                self.L_plus_W.setText("{}".format(out))
                self.L_plus_W.setStyleSheet("""background-color: white; color: red;""")

            else:
                flag_evol_L = False
                flag_evol = False
                out = 'L+W= ' + str(L_plus_W) + ' (max 1250)'
                self.L_plus_W.setText("{}".format(out))
                self.L_plus_W.setStyleSheet("""background-color: white; color: red;""")

        if H_div_L > 0.24 and H_div_L < 3.01:
            out = 'H/L= ' + str(H_div_L)

            self.H_div_L.setText("{}".format(out))
            self.H_div_L.setStyleSheet("""background-color: white; color: green;""")
        else:
            if H_div_L < 0.24:
                flag_evol_L = False
                flag_evol = False
                out = 'H/L= ' + str(H_div_L) + ' (min 0.25)'
                self.H_div_L.setText("{}".format(out))
                self.H_div_L.setStyleSheet("""background-color: white; color: red;""")

            else:
                flag_evol_L = False
                flag_evol = False
                out = 'H/L= ' + str(H_div_L) + ' (max 3)'
                self.H_div_L.setText("{}".format(out))
                self.H_div_L.setStyleSheet("""background-color: white; color: red;""")

        if H_div_W > 0.24 and H_div_W < 3.01:
            out = 'H/W= ' + str(H_div_W)
            self.H_div_W.setText("{}".format(out))
            self.H_div_W.setStyleSheet("""background-color: white; color: green;""")
        else:
            if H_div_W < 0.24:
                flag_evol_L = False
                flag_evol = False
                out = 'H/W= ' + str(H_div_W) + ' (min 0.25)'
                self.H_div_W.setText("{}".format(out))
                self.H_div_W.setStyleSheet("""background-color: white; color: red;""")

            else:
                flag_evol_L = False
                flag_evol = False
                out = 'H/W= ' + str(H_div_W) + ' (max 3)'
                self.H_div_W.setText("{}".format(out))
                self.H_div_W.setStyleSheet("""background-color: white; color: red;""")

        if L1_div_W1 > 0.24 and L1_div_W1 < 4.01:
            out = 'L1/W1= ' + str(L1_div_W1)
            self.L_div_W.setText("{}".format(out))
            self.L_div_W.setStyleSheet("""background-color: white; color: green;""")
        else:
            if L1_div_W1 < 0.24:
                flag_evol = False
                out = 'L1/W1= ' + str(L1_div_W1) + ' (min 0.25)'
                self.L_div_W.setText("{}".format(out))
                self.L_div_W.setStyleSheet("""background-color: white; color: red;""")

            else:
                flag_evol = False
                out = 'L1/W1= ' + str(L1_div_W1) + ' (max 4)'
                self.L_div_W.setText("{}".format(out))
                self.L_div_W.setStyleSheet("""background-color: white; color: red;""")

        if W2_div_L2 > 0.24 and W2_div_L2 < 4.01:
            out = 'W2/L2= ' + str(W2_div_L2)
            self.L_L_div_W.setText("{}".format(out))
            self.L_L_div_W.setStyleSheet("""background-color: white; color: green;""")
        else:
            if W2_div_L2 < 0.24:
                flag_evol_L = False
                out = 'W2/L2= ' + str(W2_div_L2) + ' (min 0.25)'
                self.L_L_div_W.setText("{}".format(out))
                self.L_L_div_W.setStyleSheet("""background-color: white; color: red;""")

            else:
                flag_evol_L = False
                out = 'W2/L2= ' + str(W2_div_L2) + ' (max 4)'
                self.L_L_div_W.setText("{}".format(out))
                self.L_L_div_W.setStyleSheet("""background-color: white; color: red;""")

        # -----------------------------доп линии -------------------------------
        #         618
        if L < 385 or L > 1835 or W < 220 or W > 600:
            flag_618 = False
        if width < 50 or width > 690 or length < 90 or length > 730 or heigth < 75 or heigth > 495 or k > 280:
            flag_618 = False
        #         924
        if L < 850 or L > 2435 or W < 300 or W > 920:
            flag_924 = False
        if width < 120 or width > 1080 or length < 120 or length > 1080 or heigth < 105 or heigth > 800 or k > 350:
            flag_924 = False
        #         1228
        if L < 700 or L > 2835 or W < 350 or W > 1500:
            flag_1228 = False
        if width < 120 or width > 1225 or length < 175 or length > 1280 or heigth < 105 or heigth > 1280 or k > 700:
            flag_1228 = False
        if S < 0.5:
            self.error_sq_1228.setGeometry(QtCore.QRect(190, 650, 150, 41))
            self.error_sq_1228.setText("{}".format('S = ' + str(S) + '  (<0.5)'))
            self.error_sq_1228.setStyleSheet("""background-color: white; color: red;""")
        else:
            self.error_sq_1228.clear()

        # -----------------------------отображение линий-------------------------------
        if flag_evol:
            self.line_EVOL.setStyleSheet(""" color: green;""")
        else:
            self.line_EVOL.setStyleSheet(""" color: red;""")

        if flag_evol_L:
            self.line_EVOL_2.setStyleSheet(""" color: green;""")
        else:
            self.line_EVOL_2.setStyleSheet(""" color: red;""")

        if flag_618:
            self.line_618.setStyleSheet(""" color: green;""")
        else:
            self.line_618.setStyleSheet(""" color: red;""")

        if flag_924:
            self.line_924.setStyleSheet(""" color: green;""")
        else:
            self.line_924.setStyleSheet(""" color: red;""")

        if flag_1228:
            self.line_1228.setStyleSheet(""" color: green;""")
        else:
            self.line_1228.setStyleSheet(""" color: red;""")

        if flag_bobst:
            self.line_bobst.setStyleSheet(""" color: green;""")
        else:
            self.line_bobst.setStyleSheet(""" color: black;""")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
