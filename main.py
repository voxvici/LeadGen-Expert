from PyQt5 import QtCore, QtGui, QtWidgets
import source_rc

import os
import re
import csv
import random

from googlesearch import search
from bs4 import BeautifulSoup
import requests


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(847, 512))
        MainWindow.setMaximumSize(QtCore.QSize(847, 512))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voxviciblue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(41, 44, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-20, -10, 271, 191))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setStyleSheet("image: url(:/LeadGenLogo/logo.jpg);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        
        self.mainInput = QtWidgets.QLineEdit(self.centralwidget)
        self.mainInput.setGeometry(QtCore.QRect(270, 180, 541, 61))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainInput.sizePolicy().hasHeightForWidth())
        
        self.mainInput.setSizePolicy(sizePolicy)
        self.mainInput.setStyleSheet("background-color: rgb(41, 44, 51);\n"
        "color: rgb(255, 255, 255);\n"
        "border:2px solid;\n"
        "border-radius:6px;\n"
        "border-color: rgb(192, 192, 0);\n"
        "font: 25 21pt \"Segoe UI Light\";")
        self.mainInput.setPlaceholderText("")
        self.mainInput.setObjectName("mainInput")
        self.mainInputTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainInputTitle.setGeometry(QtCore.QRect(270, 90, 531, 41))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainInputTitle.sizePolicy().hasHeightForWidth())
        
        self.mainInputTitle.setSizePolicy(sizePolicy)
        self.mainInputTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25 21pt \"Segoe UI Light\";")
        self.mainInputTitle.setObjectName("mainInputTitle")
        
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(270, 260, 541, 91))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSearch.sizePolicy().hasHeightForWidth())
        
        self.pushButtonSearch.setSizePolicy(sizePolicy)
        self.pushButtonSearch.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(192, 192, 0);\n"
        "border:1px solid;\n"
        "border-color: rgb(192, 192, 0);\n"
        "border-radius:6px;\n"
        "font: 25 30pt \"Segoe UI Light\";")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonSearch.clicked.connect(self.begin_search)
        
        self.aboutLabel = QtWidgets.QLabel(self.centralwidget)
        self.aboutLabel.setGeometry(QtCore.QRect(60, 410, 111, 41))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutLabel.sizePolicy().hasHeightForWidth())
        
        self.aboutLabel.setSizePolicy(sizePolicy)
        self.aboutLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25 27pt \"Segoe UI Light\";")
        self.aboutLabel.setObjectName("aboutLabel")
        
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(10, 220, 221, 181))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        
        self.aboutButton.setSizePolicy(sizePolicy)
        self.aboutButton.setStyleSheet("color: rgb(255, 0, 0);\n"
        "background-color: rgb(41, 44, 51);\n"
        "border:none;\n"
        "image: url(:/Voxvici/voxviciblue.jpg);")
        self.aboutButton.setText("")
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.clicked.connect(self.about_frame_show)
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 370, 541, 51))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("border: none;\n text-align: center;")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, -10, 601, 501))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.hide()
        
        self.aboutLabel_2 = QtWidgets.QLabel(self.frame)
        self.aboutLabel_2.setGeometry(QtCore.QRect(120, 230, 351, 41))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutLabel_2.sizePolicy().hasHeightForWidth())
        
        self.aboutLabel_2.setSizePolicy(sizePolicy)
        self.aboutLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 25 27pt \"Segoe UI Light\";")
        self.aboutLabel_2.setObjectName("aboutLabel_2")
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(520, 20, 89, 25))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("border: none;\n"
        "image: url(:/GoBack/goback.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.about_frame_hide)
        
        self.mainInput.raise_()
        self.mainInputTitle.raise_()
        self.pushButtonSearch.raise_()
        self.logo.raise_()
        self.aboutLabel.raise_()
        self.aboutButton.raise_()
        self.progressBar.raise_()
        self.frame.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lead Generation Expert"))
        self.mainInput.setText(_translate("MainWindow", "Your Industry"))
        self.mainInputTitle.setText(_translate("MainWindow", "Where you wanna export leads from?"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.aboutLabel.setText(_translate("MainWindow", "About"))
        self.aboutLabel_2.setText(_translate("MainWindow", "github.com/voxvici"))

    def about_frame_show(self):
        self.frame.show()

    def about_frame_hide(self):
        self.frame.hide()

    def begin_search(self):

        self.beginProgress = random.randint(1,31)
        self.progressBar.setValue(self.beginProgress)

        userinput = self.mainInput.text()

        if not os.path.exists('DATA'):
            os.mkdir('DATA')

        csvFile = open('DATA/data.csv', 'a', encoding='utf-8')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['URL', 'NAME', 'DESCRIPTION', 'EMAIL', 'PHONE1', 'PHONE2', 'PHONE3'])

        def findURL(tag, n, language):
            urls = [url for url in search(tag, stop=n, lang=language)][:n]
            return urls

        urls = findURL(userinput + 'company about contact', 9, 'en')

        try:
            for url in urls:

                source = requests.get(url).text
                soup = BeautifulSoup(source, 'html.parser')

                title = soup.find_all('title')

                email = soup.find_all('a')
                emailList = re.findall(r'\w+@\w+\.{1}\w+', str(email))

                phone1 = soup.find_all('p')
                phone1List = re.findall(r'T.+[\d.]+[\d.]+-[\d.]', str(phone1))
                phone3List = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', str(phone1))

                phone2 = soup.find_all('h3')
                phone2List = re.findall(r'[\d.]+[\d.]+-[\d.]+[\d.]', str(phone2))

                descr = soup.find_all('meta')
                descrList = [meta.attrs['content'] for meta in descr if 'name' in meta.attrs and meta.attrs['name'] == 'description']

                csvWriter.writerow([url, title, descrList, emailList, phone1List, phone2List, phone3List])          
        
        except Exception:
            self.mainInput.setText('Umm?')

        csvFile.close()

        self.progressBar.setValue(100)
        self.mainInput.setText('Done! Check DATA/data.csv')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
