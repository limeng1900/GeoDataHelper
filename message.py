from PyQt5.QtWidgets import QMessageBox

def error_msg (obj, msg):
    QMessageBox.warning(obj, 'error', msg, QMessageBox.Ok,QMessageBox.Ok)

