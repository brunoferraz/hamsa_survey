# # from . import question
# from .. import question
# # from ..question import IQuestion
# from ...hamsa import question

from ..question import IQuestion
# class IQuestion():
#     def __init__(self):
        
#         pass
#     pass
# class ClosedQuestion(question.IQuestion):
#     def __init__(self, value, _label = None, _type = None, _question = None):
#         pass
class ClosedQuestion(IQuestion.Abstract):
    def __init__(self):
        pass
    pass