from PyQt5.QtCore import pyqtSlot,QMetaObject
from PyQt5.QtWidgets import QDialog,QFileDialog
from views.input_dialog_view_ui import UI_FileDialog
from message import error_msg

class InputDialog(QDialog):

    def __init__(self, model, controller):
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = UI_FileDialog()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.buttonBox.accepted.connect(lambda: self.accept(self._ui))
        self._ui.pushButton.clicked.connect(self.openfile)

        # listen for model event signals
        self._model.file_path_changed.connect(self.on_file_path_changed)
        self._model.coordination_change.connect(self.on_coordination_change)

    @pyqtSlot(str)
    def on_file_path_changed(self, value):
        self._ui.textEdit.setText(value)

    @pyqtSlot(str)
    def on_coordination_change(self):
        self._model.coordination = self.coordinateSelect.currentText()
        print(self.coord)

    def openfile(self):
        openfile_path = QFileDialog.getOpenFileName(None, 'chose file', '',  '*.xlsx | *.xls | *.shp | *.geojson | *.json')
        self._model.file_path = openfile_path[0]

    # 点击OK
    def accept(self, Dialog):
        print('load data')
        if self._model.file_path:
            try:
                ext = self._model.file_path.split('.')[-1]
                if ext in ['shp', 'json', 'geojson']:
                    print('accept', self._model.file_path)
                    # self.gdf = gpd.GeoDataFrame.from_file(self.path)
                    self._controller.get_geo_dataframe()
                    self.close()
                else:
                    error_msg(Dialog, 'just support .shp .json .geojson')
            except Exception as e:
                print(e)
                error_msg(Dialog, 'file input error，please check your file')
        else:
            error_msg(Dialog, 'please chose one file')

