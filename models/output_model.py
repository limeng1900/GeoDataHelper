from PyQt5.QtCore import QObject, pyqtSignal


class OutputModel(QObject):
    file_path_changed = pyqtSignal(str)
    file_type_changed = pyqtSignal(str)
    coordination_changed = pyqtSignal(str)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
        self.file_path_changed.emit(value)

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
        self.file_type_changed.emit(value)

    @property
    def coordination(self):
        return self._coordination

    @coordination.setter
    def coordination(self, value):
        self._coordination = value
        self.coordination_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._file_path = ''
        self._file_type = ''
        self._coordination = ''
