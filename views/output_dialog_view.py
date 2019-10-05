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
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.buttonBox.accepted.connect(lambda: self.save(self._ui))
        self._ui.pushButton.clicked.connect(self.get_save_path)

        # listen for model event signals
        self._output_model.file_path_changed.connect(self.on_file_path_changed)
        self._output_model.file_type_changed.connect(self.on_file_type_changed)
        self._output_model.coordination_change.connect(self.on_coordination_change)

    @pyqtSlot(str)
    def on_file_path_changed(self, value):
        self._ui.textEdit.setText(value)

    @pyqtSlot(str)
    def on_file_type_changed(self, value):
        self._output_model.file_type = self._ui.filetypeCombobox.currentText()

    @pyqtSlot(str)
    def on_coordination_change(self):
        self._output_model.coordination = self._ui.coordinateSelect.currentText()

    def get_save_path(self):
        file_path = QFileDialog.getSaveFileName(None, 'save file')
        self._output_model.file_path = file_path[0]

    # save file
    def save(self, Dialog):
        print('save data')
        print(self._output_model.file_path)
        print(self._output_model.file_type)
        print(self._output_model.coordination)
        if not self._output_model.file_path:
            error_msg(Dialog, 'please file the output path ~')
            return
        try:
            path = self._output_model.file_path
            gdf = self._model.geo_dataframe
            file_type = self._output_model.file_type
            file_ext = CONST.FILE_EXT[file_type]
            coordination = self._output_model.coordination
            if path.split('.')[-1] != file_ext:
                path = self._output_model.file_path + '.' + file_ext
            if coordination != self._model.coordination:
                gdf = gdf.to_crs(epsg=CONST.EPSG[self._output_model.coordination])
            gdf.to_file(path, driver=file_type)
        except Exception as e:
            error_msg(Dialog, 'file output error，please check your file ~')
