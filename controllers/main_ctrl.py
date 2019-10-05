from PyQt5.QtCore import QObject, pyqtSlot
from geopandas import GeoDataFrame
from const.const import CONST


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # read file, .shp .geojson
    @pyqtSlot(object)
    def get_geo_dataframe(self):
        self._model.geo_dataframe = GeoDataFrame.from_file(self._model.file_path)
        # init coordination
        if self._model.coordination in CONST.EPSG:
            self._model.geo_dataframe.crs = {'init': 'epsg:' + str(CONST.EPSG[self._model.coordination])}
        print(self._model.geo_dataframe.head())
