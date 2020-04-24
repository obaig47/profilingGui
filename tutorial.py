from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # xpos, ypos, width, height
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Pandas Profiler")

    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(50,50)

    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
