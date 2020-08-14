import pandas as pd
import string
from . import survey
from enum import Enum
import hamsa.heuristics




class QuestionType(Enum):
    OPENED = 0
    CLOSED = 1
    CLOSED_MULTIPLE_CHOICE = 2
    CLOSED_CHECKBOX = 3


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
        s = survey.Survey(df)
        return s
    pass

def getType(answers:pd.core.series.Series = None) -> QuestionType:
    """Analizes one question's answers in order to figure out its type.

    :param Series answers: Receives one columns from panda´s dataFrame. This must be one question´s all answers.
    :return Type: Which type of question is this
    """
    # verify if its a opened or closed question
    # percent_unique = getPercentUniqueAnswer(answers=answers)
    # print(percent_unique)
    # a = answers.unique()

    # verify if its a opened or closed question
    # for i in answers:
        # print(len(i))
        # verify if all the answers has the same size
            # if not probably open
                # verify if there are some categories
                    #  if not its OPENED FOR SURE
                        # if it is opened its over for now
                    #  if YES its CLOSED FOR SURE
                        # if it is closed try to discover which kind of
    
    return QuestionType.OPENED
    pass
def getPercentUniqueAnswer(answers:pd.core.series.Series = None) -> float:
    """Use statistics from pandas to check out the percent of unique ansers

    :param Series answers: Receives one columns from panda´s dataFrame. This must be one question´s all answers.
    :return float: Percent of unique answers
    """
    # Get statistic information from answers
    # It can be acessed by the keys "count" "unique" "top" "frequency"
    print(answers)
    stat = answers.describe(include='all')
    unique = stat["unique"]
    count = stat["count"]
    hasempty = answers.isna().values.any()
    howmanyempty = answers.isna().sum()
    # check if all questions were answered
    if(hasempty):
        # YES
        howmanyanswered = count - howmanyempty
        # NOT
    else:
        howmanyanswered = count
    percent = (unique * 100) / howmanyanswered
    return percent
    pass