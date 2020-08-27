import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import numpy as np


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, header, data=None, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data
        self._header = header

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.ToolTipRole:
            # if index.column() == 2:
            #     pass
            #     # q = QtWidgets.QComboBox()
            #     # q.addItem("dsfdsfds")
            #     # q.addItem("dtytrytrfdsfs")
            #     # self.ch
            #     # return q
            # else:
            value = self._data[index.row(), index.column()]
            return str(value)
        
        if role == Qt.BackgroundRole:
            if self._data[index.row(), 3] == False or self._data[index.row(), 3] == "False":
                return QtGui.QColor("#DDDDDD")

            
        
        # if role == Qt.BackgroundRole:
        #     self._data[index.row(), 3]

    def headerData(self, section,  orientation, role):
        if role != Qt.DisplayRole:
            return None

        if (orientation == Qt.Horizontal) and (section < len(self._header)):
            return self._header[section]
        
        if (orientation == Qt.Vertical) and (section < len(self._data)):
            return section

        return None 
        # super().headerData(section, orientation, role)
    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            self._data[index.row()][index.column()] = value
            return True
        else:
            return False

    def rowCount(self, index):
        return self._data.shape[0]
    #     # return 1
    #     # return len(self._data[0])

    def columnCount(self, index):
    #     # return len(self._data)
        return self._data.shape[1]
    #     # return 34
