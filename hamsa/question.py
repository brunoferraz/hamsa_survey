class IQuestion:
    """
    Abstract class for survey's questions

    :param str _label: question label to be indentified on neural network. It must be one word at last
    :param str _question:
    :param str _answer: 
    :todo: Develop methods __str__, __repr__, __call__ in order to make save and load
    """
    def __init__(self, _survey=None, _label = None, _question = None, _answer = None):
        self.survey     = _survey
        self.label      = _label
        self.question   = _question
        self.answer     = _answer
        pass

class OpenedQuestion(IQuestion):
    def __init__(self, _survey = None, _label = None, _question = None, _answer = None):
        super.__init__(_survey, _label, _question, _answer)
        pass
    pass
# class OpenedQuestion(IQuestion):
#     def __init__(self, _survey = None, _label = None, _question = None, _answer = None):
#         super.__init__(_survey, _label, _question, _answer):
#         pass
#     pass

# class ClosedQuestion(IQuestion):
#     def __init__(self, _survey = None, _label, _question, _answer):
#         super.__init__(_survey, _label, _survey, _question, _answer):
#         pass
#     pass