# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 350))
        MainWindow.setMaximumSize(QtCore.QSize(500, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 501, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(400, 70, 71, 21))
        self.toolButton.setObjectName("toolButton")
        self.saveTextEdit = QtWidgets.QLineEdit(self.tab)
        self.saveTextEdit.setGeometry(QtCore.QRect(90, 70, 300, 21))
        self.saveTextEdit.setObjectName("saveTextEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.downloadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(10, 120, 211, 20))
        self.checkBox.setObjectName("checkBox")
        self.urlTextEdit = QtWidgets.QLineEdit(self.tab)
        self.urlTextEdit.setGeometry(QtCore.QRect(90, 40, 300, 21))
        self.urlTextEdit.setObjectName("urlTextEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(380, 120, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.resolutionComboBox = QtWidgets.QComboBox(self.tab)
        self.resolutionComboBox.setGeometry(QtCore.QRect(380, 100, 81, 21))
        self.resolutionComboBox.setObjectName("resolutioncomboBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.fileTextEdit = QtWidgets.QLineEdit(self.tab_2)
        self.fileTextEdit.setGeometry(QtCore.QRect(90, 40, 300, 21))
        self.fileTextEdit.setObjectName("fileTextEdit")
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setGeometry(QtCore.QRect(400, 70, 71, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_7.setObjectName("label_7")
        self.savePathEdit = QtWidgets.QLineEdit(self.tab_2)
        self.savePathEdit.setGeometry(QtCore.QRect(90, 70, 300, 21))
        self.savePathEdit.setObjectName("savePathEdit")
        self.fileToolButton = QtWidgets.QToolButton(self.tab_2)
        self.fileToolButton.setGeometry(QtCore.QRect(400, 40, 71, 21))
        self.fileToolButton.setObjectName("fileToolButton")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 160, 491, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.convertButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.convertButton.setObjectName("convertButton")
        self.horizontalLayout_2.addWidget(self.convertButton)
        self.extension = QtWidgets.QComboBox(self.tab_2)
        self.extension.setGeometry(QtCore.QRect(150, 120, 81, 21))
        self.extension.setObjectName("extension")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 2620, 100))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "Browse"))
        self.downloadButton.setText(_translate("MainWindow", "Tải xuống"))
        self.checkBox.setText(_translate("MainWindow", " Đổi định dạng sau khi tải"))
        self.label_2.setText(_translate("MainWindow", " Video URL : "))
        self.label_3.setText(_translate("MainWindow", "   Lưu vào : "))
        self.label.setText(_translate("MainWindow", "Nhập URL và đường dẫn tải xuống"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tải xuống"))
        self.toolButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_6.setText(_translate("MainWindow", "   Thư mục : "))
        self.label_7.setText(_translate("MainWindow", "   Lưu vào : "))
        self.fileToolButton.setText(_translate("MainWindow", "Browse"))
        self.label_8.setText(_translate("MainWindow", "Chọn thư mục để tải xuống"))
        self.convertButton.setText(_translate("MainWindow", "Tải xuống"))
        self.label_9.setText(_translate("MainWindow", " Định dạng : "))
        self.label_10.setText(_translate("MainWindow", " Độ phân giải : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Đổi định dạng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
