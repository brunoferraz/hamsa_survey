"""Written by Bruno Ferraz (brunoferraz.pro@gmail.com)"""
import abc

class IInstance(metaclass = abc.ABCMeta):
    """
    Interface to define classes to hold and navigate through reference to surveys entries
    """
    @abc.abstractmethod
    def _pre_process(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_answer(self, columnIndex):
        raise NotImplementedError
    @abc.abstractmethod
    def get_answers(self):
        raise NotImplementedError
    @abc.abstractmethod
    def get_question(self, columnIndex):
        raise NotImplementedError
    @abc.abstractmethod
    def get_question_heading(self, columnIndex):
        raise NotImplementedError

class Instance(IInstance):
    def __init__(self, surveyParam, rowIndex:int):
        import hamsa.survey
        self.__survey__           = surveyParam
        self.__rowIndex__         = rowIndex
        self._pre_process()
    def _pre_process(self):

        pass
    def get_answer(self):
        
        pass
    def get_answers(self):
        return self.__survey__.get_instance_raw_answers(self.__rowIndex__)
        
    def get_question(self):

        pass
    def get_question_heading(self):

        pass