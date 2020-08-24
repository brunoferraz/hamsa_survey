import abc
from enum import Enum
from hamsa import heuristics


"""
ABSTRACTION SECTION
"""
class IQuestionState(metaclass = abc.ABCMeta):
    """
    Interface to define the methods used to decode answers from string base.
    The behavior used to this processed will change due to the question type.
    This abstraction works like a Type for the question. 
    """
    @abc.abstractmethod
    def get_answers(self):
        raise NotImplementedError

class QuestionType(Enum):
    UNKNOW = 0
    OPENED = 1
    CLOSED = 2
    CLOSED_MULTIPLE_CHOICE = 3
    CLOSED_CHECKBOX = 4
    decode = {"0":"UNKNOW",
             "1":"OPENED", 
             "2":"CLOSED", 
             "3":"CLOSED_MULTIPLE_CHOICE",
             "4":"CLOSED_CHECKBOX"}
    # print(self.__questionType__)
    # print(repr(self.__questionType__))
    # print(self.__questionType__.value)
    # https://docs.python.org/3/library/enum.html

class IQuestion(metaclass = abc.ABCMeta):
    """
    Public Methods
    """
    @abc.abstractmethod
    def get_id(self)->int:
        raise NotImplementedError
    @abc.abstractmethod
    def get_label(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_heading(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_type_string(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_raw_answers(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def get_answers(self, i:int):
        raise NotImplementedError
    @abc.abstractmethod
    def change_type(self):
        raise NotImplementedError
    
    """
    Private Methods
    """
    @abc.abstractmethod
    def _create_type(self):
        raise NotImplementedError
    @abc.abstractmethod
    def _remove_type(self):
        raise NotImplementedError
    @abc.abstractmethod
    def _figure_out_type(self):
        raise NotImplementedError


"""
CONCRETE SECTION
"""
class OpenEndedQuestion(IQuestionState):
    def get_answers(self):
        pass

class ClosedEndedQuestion(IQuestionState):
    def get_answers(self):
        pass

class Question(IQuestion):
    def __init__(self, surveyParam, columnIndex:int, questionLabel:str):
        import hamsa.survey
        self.__id__             = None
        self.__survey__         = surveyParam
        self.__questionType__   = QuestionType.UNKNOW
        self.__columnIndex__    = columnIndex
        self.__questionlabel__  = questionLabel
        self.__listStates__     = {}
        print(self.__questionType__)
        self.change_type(self._figure_out_type())
        print(self.__questionType__)
        pass
    """
    PUBLIC IMPLEMENTATIONS
    """
    def get_id(self):
        pass
    def get_label(self):
        pass
    def get_heading(self):
        pass
    def get_type(self):
        """
        Method to get the question type

        :return QuestionType: Enum that indicate the type. Must be decoded
        """
        return self.__questionType__
    def get_type_string(self):
        """
        Method to get the question type already decoded into string

        :return str: QuestionType enum decoded
        """
        return QuestionType.decode(self.__questionType__)

    def get_raw_answers(self):
        return self.__survey__.get_question_raw_answers(self.__columnIndex__)
        
    def get_answers(self):

        pass
    def change_type(self, questionTypeParam:QuestionType):
        """
        Method used to change question type
        """
        self.__questionType__ = questionTypeParam
        self._create_type(questionTypeParam)
        pass
    
    """
    PRIVATE IMPLEMENTATIONS
    """
    def _create_type(self, questionTypeParam:QuestionType):
        """
        Method that create Question types and register it into a Dictionary
        If the method has been created before, nothing happens
        """
        if(questionTypeParam == QuestionType.OPENED):
            self.__listStates__.setdefault(QuestionType.OPENED, OpenEndedQuestion())
        elif(questionTypeParam == QuestionType.OPENED):
            self.__listStates__.setdefault(QuestionType.CLOSED, ClosedEndedQuestion())
    def _remove_type(self, questionTypeParam):
        if(questionTypeParam in self.__listStates__):
            del self.__listStates__[questionTypeParam]
        pass
    
    def _figure_out_type(self):
        answers = self.get_raw_answers()
        unique  = len(answers.unique())
        count   = answers.count()
        percent = (unique*100) / count
        if(percent > heuristics.THRESHOLD_UNIQUE):
            return QuestionType.OPENED
        else:
            return QuestionType.CLOSED
        pass

# import  hamsa as hs
# from . import survey
# class IQuestion:
#     """
#     Abstract class for survey's questions

#     :param str _survey: question label to be indentified on neural network. It must be one word at last
#     :param str _question:
#     :param str _columnIndex: 
#     :todo: Develop methods __str__, __repr__, __call__ in order to make save and load
#     """
#     def __init__(self, _survey =None, _label = None, _columnIndex = None):
#         self.surveyPointer  = _survey
#         self.label          = _label
#         self.columnIndex    = _columnIndex
#         self.type           = hs.QuestionType.UNKNOW
#         self.enable         = True
#         pass
#     def getQuestion(self):
#         """
#         Return the question text

#         :return str: This question's text
#         """
#         return self.surveyPointer.getQuestion(self.columnIndex)
#     # def __str__(self):
#     #     text = ""
#     #     text = text + str(self.label) + "\n"
#     #     text = text + str(self.type) + "\n"
#     #     text = text + str(self.question)
#     #     return text

# class OpenedQuestion(IQuestion):
#     def __init__(self, _survey = None, _label = None,_columnIndex = None):
#         super().__init__(_survey, _label, _columnIndex)
#         self.type = hs.QuestionType.OPENED
#         pass
#     pass

# class ClosedQuestion(IQuestion):
#     def __init__(self, _survey = None, _label = None,_columnIndex = None):
#         super().__init__(_survey, _label, _columnIndex)
#         self.type = hs.QuestionType.CLOSED
#         pass
#     pass