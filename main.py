import sys
from PyQt4 import QtGui, QtCore  # QtCore is for event handling
from PyQt4.QtGui import QFileDialog


class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.initUI()

    def initUI(self):

        # Main Window
        # self.resize(320, 240)
        self.setGeometry(0, 0, 320, 175)
        self.setWindowTitle('Data Profiler')
        self.setWindowIcon(QtGui.QIcon('server.png'))
        self.center()

        # Toolbar
        # toolBar = self.addToolBar('Main Toolbar')
        # extractAction = QtGui.QAction(QtGui.QIcon('open_xlsx.png'), 'Load Excel File', self)
        # extractAction.triggered.connect(self.close_application)
        # toolBar.addAction(extractAction)

        # QtGui.QWidget.__init__(self)
        self.excel_btn = QtGui.QPushButton('Load Excel File', self)
        self.excel_btn.clicked.connect(self.fileBrowse)
        self.excel_btn.setIcon(QtGui.QIcon('open_xlsx.png'))
        # self.button.setIconSize(QtCore.QSize(24, 24))
        # layout = QtGui.QVBoxLayout(self)
        # layout.addWidget(self.button)

        self.csv_btn = QtGui.QPushButton('Load CSV File', self)
        self.csv_btn.clicked.connect(self.fileBrowse)
        self.csv_btn.setIcon(QtGui.QIcon('open_csv.png'))
        self.csv_btn.move(100, 0)

        self.csv_btn = QtGui.QPushButton('Profile Destination', self)
        self.csv_btn.clicked.connect(self.fileBrowse)
        self.csv_btn.setIcon(QtGui.QIcon('save.png'))
        self.csv_btn.move(200, 0)

        # Progress bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(55, 70, 250, 20)

        # Convert File Button
        self.btn = QtGui.QPushButton("Create Profile", self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.fileBrowse)
        self.btn.clicked.connect(self.convert)
        self.btn.move(125, 40)

        # Opened files being stored here
        self.csv = []

        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit',
                                            "Are you sure you want to quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaoooww!!!")
            sys.exit()
        else:
            pass

    def fileBrowse(self):
        if len(self.csv) < 2:
            filePath = QtGui.QFileDialog.getOpenFileName(self,
                                                         '',
                                                         "Desktop",
                                                         '*.csv')

            if filePath != "" and not filePath in self.csv:
                self.csv.append(filePath)
        if len(self.csv) == 2:
            self.process()

    def convert(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        import pandas as pd
        from pandas import DataFrame

        df1 = pd.read_csv(self.csv[0])
        df2 = pd.read_csv(self.csv[1])

        df3 = df1.loc[:, ['a_column', 'b_column']]

        df3[""] = ""

        df4 = df2.loc[:, ['c_column', 'd_column', 'e_column']]

        new = pd.concat([df3, df4], axis=1)

        new.index = new.index + 1

        new.to_csv('csv2.csv')


def main():
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    app.exec_()


if __name__ == '__main__':
    main()
