import abc
from enum import Enum
from hamsa import heuristics


"""
ABSTRACTION SECTION
"""
class IQuestionType(metaclass = abc.ABCMeta):
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
    @abc.abstractmethod
    def get_answers_encoded(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_categories(self):
        raise NotImplementedError

class QuestionType(Enum):
    UNKNOW = 0
    OPENED = 1
    CLOSED = 2
    CLOSED_MULTIPLE_CHOICE = 3
    CLOSED_CHECKBOX = 4

decode_type_to_string = {QuestionType.UNKNOW:"UNKNOW",
             QuestionType.OPENED:"OPENED", 
             QuestionType.CLOSED:"CLOSED", 
             QuestionType.CLOSED_MULTIPLE_CHOICE:"CLOSED_MULTIPLE_CHOICE",
             QuestionType.CLOSED_CHECKBOX:"CLOSED_CHECKBOX"}

decode_string_to_type = {"UNKNOW":QuestionType.UNKNOW,
             "OPENED":QuestionType.OPENED, 
             "CLOSED":QuestionType.CLOSED, 
             "CLOSED_MULTIPLE_CHOICE":QuestionType.CLOSED_MULTIPLE_CHOICE,
             "CLOSED_CHECKBOX":QuestionType.CLOSED_CHECKBOX}

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
    def get_categories(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_type_string(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_raw_answers(self, i:int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_answers_encoded(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_state(self):
        raise NotImplementedError
    @abc.abstractmethod
    def set_state(self, state:bool):
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
    @abc.abstractmethod
    def _get_type_object(self):
        raise NotImplementedError


"""
CONCRETE SECTION
"""
class ConcreteQuestionsType(IQuestionType):
    def __init__(self, q):
        self.__question__ = q
        self.pre_process()
    def pre_process(self):
        pass
    def get_answers(self):
        pass
    def get_categories(self):
        return None
    def get_answers_encoded(self):
        pass

class OpenEndedType(ConcreteQuestionsType):
    def __init__(self, q):
        super().__init__(q)
        self.__question__.set_state(False)
    def get_answers(self):
        pass

class ClosedEndedType(ConcreteQuestionsType):
    def __init__(self, q):
        self.__categories__ = []
        super().__init__(q)
        self.__question__.set_state(False)
    def get_answers(self):
        pass
    def _extract_categories(self):
        return self.__question__.get_raw_answers().unique()
        

class ClosedEndedMultipleChoiceType(ClosedEndedType):
    def __init__(self, q):
        super().__init__(q)
        self.__question__.set_state(True)
    def pre_process(self):
        self.__categories__ = self._extract_categories()
        pass
    def get_answers(self):
        return self.__question__.get_raw_answers().copy()
    def get_answers_encoded(self):
        temp = self.get_answers()
        for i in range(len(self.__categories__)):
            temp.replace(self.__categories__[i], i, inplace = True)
        return temp
    def get_categories(self):
        return self.get_categories()

class Question(IQuestion):
    def __init__(self, surveyParam, columnIndex:int, questionLabel:str):
        import hamsa.survey
        self.__id__             = None
        self.__survey__         = surveyParam
        self.__questionType__   = QuestionType.UNKNOW
        self.__columnIndex__    = columnIndex
        self.__questionlabel__  = questionLabel
        self.__list_types__     = {}
        self.__enabled__        = True
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
        return decode_type_to_string[self.__questionType__]

    def get_raw_answers(self):
        return self.__survey__.get_question_raw_answers(self.__columnIndex__)
        
    def get_answers_encoded(self):
        temp = self._get_type_object().get_answers_encoded()
        temp.rename(self.get_label(), inplace = True)
        return temp
    def get_categories(self):
        return self._get_type_object().get_categories()

    def get_state(self):
        """
        Get the question state
        If True, it will be exported
        It False, it will not be exported
        """
        return self.__enabled__

    def set_state(self, state:bool):
        """
        Set the question state. If it join the export or not
        """
        self.__enabled__ = state
    
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
            self.__list_types__.setdefault(QuestionType.OPENED, OpenEndedType(self))
        elif(questionTypeParam == QuestionType.CLOSED):
            self.__list_types__.setdefault(QuestionType.CLOSED, ClosedEndedType(self))
        elif(questionTypeParam == QuestionType.CLOSED_MULTIPLE_CHOICE):
            self.__list_types__.setdefault(QuestionType.CLOSED_MULTIPLE_CHOICE, ClosedEndedMultipleChoiceType(self))
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
    def _get_type_object(self):
        return self.__list_types__[self.__questionType__]