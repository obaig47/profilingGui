# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# For File Dialog Box
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDesktopWidget, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.fileName = ""
        self.destinationDir = ""
        self.completed = 0
        self.minimalMode = False

        # Main Window
        MainWindow.setObjectName("Data Profiler")
        MainWindow.resize(464, 204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Centering Window
        #qtRectangle = self.frameGeometry()
        #centerPoint = QDesktopWidget().availableGeometry().center()
        #qtRectangle.moveCenter(centerPoint)
        #self.move(qtRectangle.topLeft())

        # Vertical Layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 371, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        # Load File Button
        self.load_file_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_file_button.setObjectName("load_file_button")
        self.verticalLayout.addWidget(self.load_file_button)
        self.load_file_button.clicked.connect(self.fileBrowse)

        # Minimal Mode Check Box
        self.minimal_mode_box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.minimal_mode_box.stateChanged.connect(self.clickBox)
        self.minimal_mode_box.setToolTip("Selecting this disables expensive computations (such as correlations and dynamic binning)\n and will speed up profiling for files that are too big")
        self.minimal_mode_box.setObjectName("minimal_mode_box")
        self.verticalLayout.addWidget(self.minimal_mode_box)


        # Generate Profile Button
        self.generate_profile_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generate_profile_button.setObjectName("generate_profile_button")
        self.verticalLayout.addWidget(self.generate_profile_button)
        self.generate_profile_button.clicked.connect(self.convert)

        # Progress Bar
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        # Setting central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle(_translate("Data Profiler", "Data Profiler"))

        self.load_file_button.setText(_translate("MainWindow", "Load File"))
        self.minimal_mode_box.setText(_translate("MainWindow", "Minimal Mode (Use on large files)"))
        self.generate_profile_button.setText(_translate("MainWindow", "Generate Profile"))

    def fileBrowse(self):
       # Load File Dialog
        self.fileName = QFileDialog.getOpenFileName(None,
                                               "Select Data File", "Desktop", "Data Files (*.csv *.xlsx *.xls)")
        print(self.fileName)
        # Extracting the first item in the tuple which is the filename
        self.fileName = self.fileName[0]

        # Select Destination Directory Dialog
        self.destinationDir = QFileDialog.getExistingDirectory(None, "Select Destination Directory")

        print(self.destinationDir)

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            self.minimalMode = True
        else:
            self.minimalMode = False

    def convert(self):
        self.completed = 0

        # Progress Bar Update
        while self.completed < 10:
            self.completed += 1
            self.progressBar.setValue(self.completed)

        import pandas as pd

        # Extracting file extension, calling appropriate read function
        fullPath, fileExtension = os.path.splitext(self.fileName)




        print('fileExtension: ' + fileExtension)
        if fileExtension == '.csv':
            df = pd.read_csv(self.fileName)
            print(df.head())
        elif fileExtension == '.xlsx' or fileExtension == '.xls':
            df = pd.read_excel(self.fileName)
            print(df.head())
        else:
            pass

        while self.completed < 50:
            self.completed += 1
            self.progressBar.setValue(self.completed)

        import pandas_profiling as pp

        # Getting file stem to use for the new html file being created
        fileStemArray = self.fileName.split('/')

        # Isolates the name of the file without the full path
        fileStemName = fileStemArray[len(fileStemArray) - 1]

        # This line is only used for the sake of pulling out the stemName without the full path
        stemName, fileExtension = os.path.splitext(fileStemName)


        if(self.minimalMode==False):
            # Creating profile using pandas_profiling
            profile = pp.ProfileReport(df)
        else:
            profile = pp.ProfileReport(df,minimal=True)

        while self.completed < 90:
            self.completed += 2
            self.progressBar.setValue(self.completed)

        # print('destinationDir: ' + self.destinationDir)
        export_file = self.destinationDir + '/Profile_' + stemName + '.html'
        print('export_file:' + export_file)
        profile.to_file(output_file=export_file)

        while self.completed < 100:
            self.completed += 2
            self.progressBar.setValue(self.completed)

        # Open the newly created file
        import webbrowser
        webbrowser.open('file://' + os.path.realpath(export_file))



if __name__ == "__main__":
    import sys, os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
