from PyQt5.QtCore import QObject, pyqtSlot
from geopandas import GeoDataFrame

epsg = {
    'WGS84': 4326,
    'BJ54': 4214,
    'XIAN80': 4610,
    'CGCS2000': 4490
}

class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # read file, .shp .geojson
    @pyqtSlot(object)
    def get_geo_dataframe(self):
        self._model.geo_dataframe = GeoDataFrame.from_file(self._model.file_path)
        # init coordination
        if self._model.coordination in epsg:
            self._model.geo_dataframe.crs = {'init': 'epsg:' + str(epsg[self._model.coordination])}
        print(self._model.geo_dataframe.head())

    # @pyqtSlot(int)
    # def change_amount(self, value):
    #     self._model.amount = value
    #
    #     # calculate even or odd
    #     self._model.even_odd = 'odd' if value % 2 else 'even'
    #
    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False