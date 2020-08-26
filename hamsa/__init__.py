import pandas as pd
import string
from enum import Enum
import abc
from . import heuristics
import hamsa.survey
import hamsa.question

def read_csv(path = None, token = ",",encoding ='utf8') -> survey.Survey:
    """Reads a CSV file

    :param str path: indicates the file and the path to it
    :param str token: token used to split the a file along the parsing step. The default is "," but ";" or "/t" are largely used instead. Opened questions demands diferent tokens since the interviewed could write anything. 
    :param str encoding: assign which encoding must be used along the parsing step. The default is UTF8
    :return survey.Survey: The object Survey
    """
    if(path == None):
        return 0
    else:
        df = pd.read_csv(path, encoding = encoding, sep = token)
        df.apply(lambda x: pd._lib.infer_dtype(x.values))
        s = hamsa.survey.Survey(df)
        return s
    pass