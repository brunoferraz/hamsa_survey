import pandas as pd
from . import question
import hamsa as hs



class Survey:
    """ Data Structure that stores information about how data will be exported to neural network"""

    def __init__(self, _df):
        """ Constructor for Survey Object

        :param pd.DataFrame _df: a pandas dataFrame
        """
        self.df         = _df
        self.report     = ""
        self.size       = 0
        self.list_label = []
        
        self.pre_process()
        pass
    def pre_process(self):
        """ preprocess data from pandas dataframe

        :todo: Look for false positive
        :return str: Report about colected data
        """

        # Find surveys size
        self.size = len(self.df.columns)
        # self.size = 1

        # Generate deafault labels
        for i in range(self.size):
            temp = "pergunta_" + str(i)
            self.list_label.append(temp)
        
        #iterate along columns
        for i in range(self.size):
            question = self.df.columns[i]
            # print(">>>>>>", question)
            column = self.df.iloc[:,i]
            # print(type(column))
            question_type = hs.getType(column)
            if(question_type == hs.QuestionType.OPENED):
                print(i, "opened >>" ,question)
            elif(question_type == hs.QuestionType.CLOSED):
                print(i, "closed >>" , question)
            pass
        return self.report
        pass
