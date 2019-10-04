from PyQt5.QtWidgets import QMessageBox

def error_msg (obj, msg):
    QMessageBox.information(obj, 'error', msg, QMessageBox.Yes,QMessageBox.Yes)

