from PyQt5.QtCore import QObject, pyqtSignal
from geopandas import GeoDataFrame


class Model(QObject):
    file_path_changed = pyqtSignal(str)
    coordination_changed = pyqtSignal(str)
    geo_dataframe_changed = pyqtSignal(object)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
        self.file_path_changed.emit(value)

    @property
    def coordination(self):
        return self._coordination

    @coordination.setter
    def coordination(self, value):
        self._coordination = value
        self.coordination_changed.emit(value)

    @property
    def geo_dataframe(self):
        return self._geo_dataframe

    @geo_dataframe.setter
    def geo_dataframe(self, value):
        self._geo_dataframe = value
        self.geo_dataframe_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._file_path = ''
        self._coordination = 'unkonw'
        self._geo_dataframe = GeoDataFrame()
