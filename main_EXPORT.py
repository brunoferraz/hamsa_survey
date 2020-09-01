import hamsa as hs
import pandas as pd
import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from interface.hamsaView import TableModel
# from interface.hamsaViewWidget import TableModel
# from interface.report import Ui_MainWindow
from interface.report_screen import Ui_MainWindow

# from hamsa import question

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ds = hs.read_csv("data/fofoca_ajustado.csv", token=";")
        self.summaryReport.setText(self.ds.get_report())

        data = self.ds.get_report_data()
        # print(data.shape[0])

        # self.tableWidget = QtWidgets.QTableWidget(data.shape[0],data.shape[1],self)
        # self.tableWidget = 
        # self.myTableWidget.setRowCount(data.shape[0])
        # self.myTableWidget.setColumnCount(data.shape[1])
        # self.myTableWidget.setModel()
        self.model = TableModel(["Label","Question","Type"],data, self)
        self.myTableWidget.setModel(self.model)

if __name__ == "__main__":
    ds = hs.read_csv("data/interface_example.csv", token=";")
    ds.export_to_matlab("data/matlaba.data")
    print('exported')
    # app = QtWidgets.QApplication(sys.argv)

    # window = MainWindow()
    # window.show()
    # app.exec_()

# print(tela.layou)
# f = ds.get_questions_headings()

# temp = ds.get_questions_by_type(hs.question.QuestionType.CLOSED_MULTIPLE_CHOICE)
# temp = ds.get_questions_by_type(hs.question.QuestionType.OPENED)
# print("ABERTAS")
# for i in temp:
#     print(i.get_heading())

# temp = ds.get_questions_by_type(hs.question.QuestionType.OPENED)


# df = pd.read_csv("data/fofoca_ajustado.csv", sep=";")

# print(df.columns[4])

# ds.list_questions[5].getQuestion()
# print(ds.getQuestion(7))
# ds = hs.read_csv("data/encoded.csv")
# print(ds)
# # import sys
# # print(sys.path)

# help(__builtins__)