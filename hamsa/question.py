import  hamsa as hs
from . import survey
class IQuestion:
    """
    Abstract class for survey's questions

    :param str _label: question label to be indentified on neural network. It must be one word at last
    :param str _question:
    :param str _answer: 
    :todo: Develop methods __str__, __repr__, __call__ in order to make save and load
    """
    def __init__(self, _survey =None, _label = None, _columnIndex = None):
        self.surveyPointer  = _survey
        self.label          = _label
        self.columnIndex    = _columnIndex
        self.type           = hs.QuestionType.UNKNOW
        self.enable         = True
        pass
    def getQuestion(self):
        """
        Return the question text

        :return str: This question's text
        """
        return self.surveyPointer.getQuestion(self.columnIndex)
    # def __str__(self):
    #     text = ""
    #     text = text + str(self.label) + "\n"
    #     text = text + str(self.type) + "\n"
    #     text = text + str(self.question)
    #     return text

class OpenedQuestion(IQuestion):
    def __init__(self, _survey = None, _label = None,_columnIndex = None):
        super().__init__(_survey, _label, _columnIndex)
        self.type = hs.QuestionType.OPENED
        pass
    pass

class ClosedQuestion(IQuestion):
    def __init__(self, _survey = None, _label = None,_columnIndex = None):
        super().__init__(_survey, _label, _columnIndex)
        self.type = hs.QuestionType.CLOSED
        pass
    pass