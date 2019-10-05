from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel
from views.main_view_ui import Ui_MainWindow
from views.input_dialog_view import InputDialog
from models.pandas_model import PandasModel


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._input_dialog = InputDialog(self._model, self._main_controller)

        # connect widgets to controller
        # show input dialog
        self._ui.openButton.clicked.connect(self._input_dialog.show)

        # listen for model event signals
        self._model.geo_dataframe_changed.connect(self.on_geo_dataframe_changed)

    @pyqtSlot(object)
    def on_geo_dataframe_changed(self, value):
        # show 100rows
        gdf_100_nogeom = value.head(100).drop(['geometry'], axis=1)
        model = PandasModel(gdf_100_nogeom)
        self._ui.tableView.setModel(model)
