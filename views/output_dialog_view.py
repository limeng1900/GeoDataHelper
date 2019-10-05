from PyQt5.QtCore import pyqtSlot,QMetaObject
from PyQt5.QtWidgets import QDialog,QFileDialog
from views.output_dialog_view_ui import UI_SaveDialog
from models.output_model import OutputModel
from message import error_msg
from const.const import CONST


class OutputDialog(QDialog):

    def __init__(self, model, controller):
        super().__init__()

        self._model = model
        self._output_model = OutputModel()
        self._controller = controller
        self._ui = UI_SaveDialog()
        self._ui.setupUi(self, self._model.coordination)

        # connect widgets to controller
        self._ui.buttonBox.accepted.connect(self.save)
        self._ui.pushButton.clicked.connect(self.get_save_path)
        self._ui.textEdit.textChanged.connect(self.set_file_path)
        self._ui.coordinateSelect.currentTextChanged.connect(self.set_coordination)
        self._ui.filetypeCombobox.currentTextChanged.connect(self.set_file_type)

        # listen for model event signals
        self._output_model.file_path_changed.connect(self.on_file_path_changed)
        self._output_model.file_type_changed.connect(self.on_file_type_changed)

    @pyqtSlot(str)
    def on_file_path_changed(self, value):
        file_ext = CONST.FILE_EXT[self._output_model.file_type]
        path = value
        if value.split('.')[-1] != file_ext:
            path = value + '.' + file_ext
        if path!= self._ui.textEdit.text():
            self._ui.textEdit.setText(path)
            self.set_file_path()

    @pyqtSlot(str)
    def on_file_type_changed(self, value):
        file_ext = CONST.FILE_EXT[value]
        path = self._output_model.file_path
        if path.split('.')[-1] != file_ext:
            path = path + '.' + file_ext
            self._ui.textEdit.setText(path)
            self.set_file_path()

    def set_file_path(self):
        self._output_model.file_path = self._ui.textEdit.text()

    def set_file_type(self):
        self._output_model.file_type = self._ui.filetypeCombobox.currentText()

    def set_coordination(self):
        self._output_model.coordination = self._ui.coordinateSelect.currentText()

    def get_save_path(self):
        file_path = QFileDialog.getSaveFileName(None, 'save file')
        self._output_model.file_path = file_path[0]

    # save file
    def save(self):
        if not self._output_model.file_path:
            error_msg(self, 'please file the output path ~')
            return
        try:
            path = self._output_model.file_path
            gdf = self._model.geo_dataframe
            file_type = self._output_model.file_type
            coordination = self._output_model.coordination
            if coordination != self._model.coordination:
                print('convert coordination')
                gdf = gdf.to_crs(epsg=CONST.EPSG[self._output_model.coordination])
            gdf.to_file(path, driver=file_type)
        except Exception as e:
            print(e)
            error_msg(self, 'file output error ~')
