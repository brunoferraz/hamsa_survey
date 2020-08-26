import abc
import pandas as pd
import hamsa
import hamsa.question
import hamsa.instance

class ISurvey(metaclass = abc.ABCMeta):
    """ Interface works as a FAÇADE for hamsa survey system. Futhermore, also works as MODEL from MVC pattern"""
    @abc.abstractmethod
    def pre_process(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_question(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_question_heading(self, i:int):
        raise NotImplementedError


    @abc.abstractmethod
    def get_questions(self) -> list:
        raise NotImplementedError
    @abc.abstractmethod
    def get_questions_headings(self) -> list:
        raise NotImplementedError
    @abc.abstractmethod
    def get_questions_by_type(self) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def get_instance(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_answer(self, i:int, j:int):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_question_raw_answers(self, columnParam:int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_instance_raw_answers(self, rowindex:int):
        raise NotImplementedError



    @abc.abstractmethod
    def get_report(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _generate_statistics(self):
        raise NotImplementedError


class Survey(ISurvey):
    """
    Data Structure that stores information about how data will be exported to neural network
    """
    def __init__(self, df):
        self.__df               = df
        self.__list_questions__ = []
        self.__list_instances__ = []
        self.__info__           = {}

        self.pre_process()
        self._generate_statistics()

    def pre_process(self):
        """
        Pre-process the data provided figuring out the questions type
        """
        size = len(self.__df.columns)
        # size = 1
        for i in range(size):
            label       = "pergunta_" + str(i)
            temp        = hamsa.question.Question(self, i, str(label))
            self.__list_questions__.append(temp)
        for i in range(len(self.__df.index)):
            temp = hamsa.instance.Instance(self, i)
            self.__list_instances__.append(temp)
        pass

    def get_question(self, index):
        """
        Get a Question object from the pre-processed list

        :param index: Question's index position
        :return Question: Question object referenced by index
        """
        return self.__list_questions__[index]

    def get_question_heading(self, index):
        """
        Get specific question's heading referenced by the index
        
        :param int index: Index position that
        """
        return self.__df.columns[index]

    def get_questions(self) -> list:
        """
        Get a list of pre-processed question

        :return list: Questions pre-processed
        """
        return self.__list_questions__

    def get_questions_headings(self) -> list:
        """
        Get a list with question's headings

        :return list: Question's Headings
        """
        temp = []
        for i in range(len(self.__list_questions__)):
            temp.append(self.get_question_heading(i))
        return temp

    def get_questions_by_type(self, typewanted:hamsa.question.QuestionType)-> list:
        """
        Get a list of questions filtered by type

        :param QuestionType typewanted:
        :return list: Questions filtered by given type
        """
        list_temp = []
        for  i in self.__list_questions__:
            if(i.get_type() == typewanted):
                list_temp.append(i)
        return list_temp

    def get_instance(self, rowindex):
        """
        Get a Instance object from the list

        :return Instance:
        """
        return self.__list_instances__[rowindex]

    def get_answer(self, lineParam, columnParam):
        """
        Get an specific an answer from a specific question
        
        :param int lineParam: line requested
        :param int columnParam: column requested
        :return str: Answer requested
        """
        return self.__df.iloc[lineParam,columnParam]

    def get_question_raw_answers(self, columnParam) -> pd.Series:
        """
        Get answers from a specific question
        
        :param int columnParam: column requested
        :return pandas.Series: answers organized in a pandas.Series
        """
        return self.__df.iloc[:,columnParam]

    def get_instance_raw_answers(self, rowindex):
        """
        Get answers from a specific instance

        :param int rowindex: index requested
        :return list: answers organizes in a list
        """
        return self.__df.iloc[rowindex].values.tolist()

    def get_report(self):
        """
        Generate statistics based on the data provided and return it as a string

        :return str: report string
        """
        self._generate_statistics()
        text = ""
        for key in self.__info__:
            text = text + str(key) + " >>>> " + str(self.__info__[key]) + "\n"
        return text

    def _generate_statistics(self):
        """
        This method is used to colect statistical information from survey and store it into __info__ dict
        """
        self.__info__["num_entries"]  = len(self.__df.index)
        self.__info__["num_question"] = len(self.__df.columns)
        openended = 0
        closedended = 0
        multiplechoice = 0
        for i in self.__list_questions__:
            if(i.get_type() == hamsa.question.QuestionType.OPENED):
                openended = openended + 1
            elif(i.get_type() == hamsa.question.QuestionType.CLOSED):
                closedended = closedended + 1
            elif(i.get_type() == hamsa.question.QuestionType.CLOSED_MULTIPLE_CHOICE):
                multiplechoice = multiplechoice + 1

        self.__info__["num_openended_questions"]        = openended
        self.__info__["num_closedended_questions"]      = closedended
        self.__info__["num_multiplechoice_questions"]   = multiplechoice