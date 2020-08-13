import pandas as pd
from . import question


class Survey:
    """ Data Structure that stores information about how data will be exported to neural network"""

    def __init__(self, _df):
        """ Constructor for Survey Object

        :param pd.DataFrame _df: a pandas dataFrame
        """
        self.df     = _df
        self.report = ""
        self.pre_process()
        
        pass
    def pre_process(self):
        """ preprocess data from pandas dataframe

        :return str: Report about colected data
        """
        print(self.df)
        
        return self.report
        pass
