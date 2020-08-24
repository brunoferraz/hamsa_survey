import abc
import pandas as pd
import hamsa
import hamsa.question

class ISurvey(metaclass = abc.ABCMeta):
    """ Interface works as a FAÇADE for hamsa survey system. Futhermore, also works as MODEL from MVC pattern"""
    @abc.abstractmethod
    def pre_process(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_questions(self) -> list:
        raise NotImplementedError
    @abc.abstractmethod
    def get_questions_headings(self) -> list:
        raise NotImplementedError
    @abc.abstractmethod
    def get_question(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_instance(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_answer(self, i:int, j:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_question_raw_answers(self, i:int):
        raise NotImplementedError

class Survey(ISurvey):
    """ Data Structure that stores information about how data will be exported to neural network"""
    def __init__(self, df):
        
        self.__df       = df
        self.pre_process()
    def pre_process(self):
        size = len(self.__df.columns)
        size = 1
        for i in range(size):
            label       = "pergunta_" + str(i)
            # question    = self.__df.columns[i]
            # column      = self.__df.iloc[:,i]
            temp        = hamsa.question.Question(self, i, str(label))
            

        pass
    def get_questions(self, i:int):
        pass
    def get_questions_headings(self):
        pass
    def get_question(self):
        pass
    def get_instance(self, i):
        pass
    def get_answer(self, i, j):
        pass
    def get_question_raw_answers(self, i) -> pd.Series:
        """
        Get answers from a specific question

        :return pandas.Series: answers organized in a pandas.Series
        """
        return self.__df.iloc[:,i]

# import pandas as pd
# import hamsa as hs
# from . import question

# class Survey:
#     """ Data Structure that stores information about how data will be exported to neural network"""

#     def __init__(self, _df):
#         """ Constructor for Survey Object

#         :param pd.DataFrame _df: a pandas dataFrame
#         """
#         self.df         = _df
#         self.report     = {}
#         self.size       = 0
#         self.list_label = []
#         self.list_questions = []
#         self.list_opened_questions = []
#         self.list_closed_questions = []
#         self.pre_process()
#         pass
#     def pre_process(self):
#         """ preprocess data from pandas dataframe

#         This method try to figure out which type of each question. Its uses the Heuristic stored at THRESHOLD_UNIQUE.If you have more unique answers than the THRESHOLD_UNIQUE probably you have a opened question otherwise you probably you have a closed question.
#         Since there are kinds of closed questions that commomly produces unique questions due to the huge number of categories combined, This step works like an oriented guess needed to be reviewed

#         :todo: Look for false positive
#         :return str: Report about colected data
#         """
#         # Find surveys size
#         self.size = len(self.df.columns)
#         # self.size = 1

#         # Generate deafault labels
#         for i in range(self.size):
#             temp = "pergunta_" + str(i)
#             self.list_label.append(temp)
        
#         #iterate along columns
#         for i in range(self.size):
#             question = self.df.columns[i]
#             # print(">>>>>>", question)
#             column = self.df.iloc[:,i]
#             # print(type(column))
#             question_type = hs.getType(column)
#             temp = ""
#             if(question_type == hs.QuestionType.OPENED):
#                 temp = hs.question.OpenedQuestion(self, self.list_label[i], i)
#                 self.list_opened_questions.append(i)
#             elif(question_type == hs.QuestionType.CLOSED):
#                 temp = hs.question.ClosedQuestion(self, self.list_label[i], i)
#                 self.list_closed_questions.append(i)
#             self.list_questions.append(temp)
#         self.report["size"] = self.size
#         self.report["openQuestions"] = len(self.list_opened_questions)
#         self.report["closedQuestions"] = len(self.list_closed_questions)
#         return self.report
    
#     def getReportFormated(self):
        
#         pass
    
#     def getQuestion(self, ind):
#         """
#         Query the question question using the index passed as parameter

#         :param int ind: Index used to query the question from dataframe
#         :return: question from the index question passed as parameter
#         """
#         return self.df.columns.values[ind]

#     def getData(self, row, column):
#         """
#         Query for some data from data frame using row and column as parameters

#         :param int row: row you want data from
#         :param int column: column you want data from
#         :return: data from the row and column passed
#         """
#         r = self.df.iloc[row, column]
#         return r

