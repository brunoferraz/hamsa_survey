import hamsa as hs
import pandas as pd
import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from interface.hamsaView import TableModel
from interface.report_screen import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ds = hs.read_csv("data/fofoca_ajustado.csv", token=";")
        self.summaryReport.setText(self.ds.get_report())

        data = self.ds.get_report_data()
        self.model = TableModel(["Label","Question","Type"],data, self)
        self.myTableWidget.setModel(self.model)

if __name__ == "__main__":
    ds = hs.read_csv("data/interface_example.csv", token=";")
    ds.export_to_matlab("data/matlaba.data")