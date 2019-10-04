from mainWindow import Ui_MainWindow
from fileDialog import FileDialog
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

class openDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=FileDialog()
        self.child.setupUi(self)

class MainWindow():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = parentWindow()
        self.open_dialog = openDialog()

    def bind_dialog(self):
        btn = self.window.main_ui.openButton
        btn.clicked.connect(self.open_dialog.show)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())


if __name__=='__main__':
    main_window = MainWindow()
    main_window.bind_dialog()
    main_window.show()


