from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow
from views.input_dialog_view import InputDialog
from views.output_dialog_view import OutputDialog
from models.pandas_model import PandasModel
from message import error_msg


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # init dialog
        self._input_dialog = InputDialog(self._model, self._main_controller)
        self._output_dialog = OutputDialog(self._model, self._main_controller)

        # connect widgets to controller
        #   show input dialog
        self._ui.openButton.clicked.connect(self._input_dialog.show)
        #   show output dialog
        self._ui.saveButton.clicked.connect(self.open_save_dialog)

        # listen for model event signals
        self._model.geo_dataframe_changed.connect(self.on_geo_dataframe_changed)

    @pyqtSlot(object)
    def on_geo_dataframe_changed(self, value):
        # show 100rows
        gdf_100_nogeom = value.head(100).drop(['geometry'], axis=1)
        model = PandasModel(gdf_100_nogeom)
        self._ui.tableView.setModel(model)

    # show save dialog
    def open_save_dialog(self):
        if self._model.geo_dataframe.empty:
            error_msg(self, 'no file to output')
        else:
            self._output_dialog.show()

