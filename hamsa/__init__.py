import pandas as pd
import string
from . import survey

def read_csv(path = None) -> survey.Survey:
    """Reads a CSV file

    :param str path: indicates the file and the path to it
    :return survey.Survey: The object Survey
    """
    if(path == None):
        return 0
    else:
        df = pd.read_csv(path)
        s = survey.Survey(df)
        return s
    pass