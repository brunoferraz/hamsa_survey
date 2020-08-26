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
    def pre_process(self):
        raise NotImplementedError
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
class ConcreteQuestionsState(IQuestionState):
    def __init__(self, q):
        self.__question__ = q
        self.pre_process()
    def pre_process(self):
        pass
    def get_answers(self):
        pass
class OpenEndedState(ConcreteQuestionsState):
    def get_answers(self):
        pass

class ClosedEndedState(ConcreteQuestionsState):
    def __init__(self, q):
        super().__init__(q)
        self.__categories__ = []
    def get_answers(self):
        pass
class ClosedEndedMultipleChoiceState(ClosedEndedState):
    def pre_process(self):
        self.__categories__ = self.get_categories()
        pass
    def get_answers(self):
        pass
    def get_categories(self):
        return self.__question__.get_raw_answers().unique()

class Question(IQuestion):
    def __init__(self, surveyParam, columnIndex:int, questionLabel:str):
        import hamsa.survey
        self.__id__             = None
        self.__survey__         = surveyParam
        self.__questionType__   = QuestionType.UNKNOW
        self.__columnIndex__    = columnIndex
        self.__questionlabel__  = questionLabel
        self.__list_types__     = {}
        self.change_type(self._figure_out_type())
        pass
    """
    PUBLIC IMPLEMENTATIONS
    """
    def get_id(self):
        return self.__id__

    def get_label(self):
        return self.__questionlabel__

    def get_heading(self):
        return self.__survey__.get_question_heading(self.__columnIndex__)

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
        Method used to change question type. It already invoke the the private method _create_type. 
        There, the state will be created since it have not been created already

        :param QuestionType questionTypeParam: Type of question you want to change into. 
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

        :param QuestionType questionTypeParam: Type of question you want to change into. 
        """
        if(questionTypeParam == QuestionType.OPENED):
            self.__list_types__.setdefault(QuestionType.OPENED, OpenEndedState(self))
        elif(questionTypeParam == QuestionType.OPENED):
            self.__list_types__.setdefault(QuestionType.CLOSED, ClosedEndedState(self))
        elif(questionTypeParam == QuestionType.CLOSED_MULTIPLE_CHOICE):
            self.__list_types__.setdefault(QuestionType.CLOSED_MULTIPLE_CHOICE, ClosedEndedMultipleChoiceState(self))
    def _remove_type(self, questionTypeParam):
        """
        Remove an existing QuestionType from the list
        """
        if(questionTypeParam in self.__list_types__):
            del self.__list_types__[questionTypeParam]
        pass
    
    def _figure_out_type(self):
        """
        Private method to figure out if the question is open-ended or closed-ended.
        It is decided based on similarity between answers
        """
        answers = self.get_raw_answers()
        unique  = len(answers.unique())
        count   = answers.count()
        percent = (unique*100) / count
        if(percent > heuristics.THRESHOLD_UNIQUE):
            return QuestionType.OPENED
        else:
            if(unique < heuristics.THRESHOLD_UNIQUE_MULTIPLE_CHOICE):
                return QuestionType.CLOSED_MULTIPLE_CHOICE
            else:
                return QuestionType.CLOSED
        pass