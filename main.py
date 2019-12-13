import sys, os
from PyQt4 import QtGui, QtCore  # QtCore is for event handling
from PyQt4.QtGui import QFileDialog, QMessageBox, QLabel


class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        # Static variables
        self.destinationDir = ""
        self.fileName = ""
        self.completed = 0
        self.load_btn = QtGui.QPushButton('Load Data File', self)
        self.profile_btn = QtGui.QPushButton("Create Profile", self)
        self.progress = QtGui.QProgressBar(self)
        self.l1 = QLabel()

        self.initUI()

    def initUI(self):

        # Main Window
        self.setGeometry(0, 0, 320, 175)
        self.setWindowTitle('Data Profiler')
        self.setWindowIcon(QtGui.QIcon('server.png'))
        self.center()

        # Load Data File Button
        self.load_btn.setGeometry(0, 0, 320, 30)
        self.load_btn.clicked.connect(self.fileBrowse)
        self.load_btn.setIcon(QtGui.QIcon('open_xlsx.png'))

        # Progress bar
        self.progress.setGeometry(55, 70, 250, 20)

        # Convert File Button
        self.profile_btn.setGeometry(0, 30, 320, 30)
        self.profile_btn.clicked.connect(self.convert)
        self.profile_btn.setIcon(QtGui.QIcon('effort.png'))

        # Text Label
        # self.l1.setText(self.fileName)
        # self.l1.setAlignment(self.AlignCenter)

        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    # def close_application(self):
    #     choice = QtGui.QMessageBox.question(None, 'Exit',
    #                                         "Are you sure you want to quit?",
    #                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    #
    #     if choice == QtGui.QMessageBox.Yes:
    #         print("Selected Yes to quit from QMessageBox")
    #         sys.exit()
    #     else:
    #         pass

    def fileBrowse(self):
        # Load File Dialog
        fileName = QFileDialog.getOpenFileName(None,
                                               "Select Data File", "Desktop", "Data Files (*.csv *.xlsx *.xls)")

        self.fileName = fileName
        # print(self.fileName)

        # Select Destination Directory Dialog
        directory = QFileDialog.getExistingDirectory(None, "Select Destination Directory")

        self.destinationDir = directory
        # print(self.destinationDir)

    def convert(self):
        self.completed = 0

        # Progress Bar Update
        while self.completed < 10:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

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
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        import pandas_profiling as pp

        # Getting file stem to use for the new html file being created
        fileStemArray = self.fileName.split('/')

        # Isolates the name of the file without the full path
        fileStemName = fileStemArray[len(fileStemArray) - 1]

        # This line is only used for the sake of pulling out the stemName without the full path
        stemName, fileExtension = os.path.splitext(fileStemName)

        # Creating profile using pandas_profiling
        profile = pp.ProfileReport(df)

        while self.completed < 90:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        # print('destinationDir: ' + self.destinationDir)
        export_file = self.destinationDir + '\\Profile_' + stemName + '.html'
        print('export_file:' + export_file)
        profile.to_file(output_file=export_file)

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        # Open the newly created file
        import webbrowser
        webbrowser.open('file://' + os.path.realpath(export_file))


def main():
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    app.exec_()


if __name__ == '__main__':
    main()
