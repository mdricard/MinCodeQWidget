import sys
from PyQt5.QtWidgets import QApplication, QWidget, QAction
from PyQt5.Qt import QLabel


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My very cool python app')
        self.resize(1000, 800)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()                     # create an instance of GUI class
    gui.show()                      # show the constructed window
    sys.exit(app.exec_())           # execute the application