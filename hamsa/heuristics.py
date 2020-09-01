"""Written by Bruno Ferraz (brunoferraz.pro@gmail.com)"""
"""
This module is used to store all heuristics values as constants.

:constant int THRESHOLD_UNIQUE: Threshold used to identify opened questions. If you have more unique answers than the THRESHOLD_UNIQUE probably you have a opened question. The threshold is expressed in percent.
"""
THRESHOLD_UNIQUE = 50
"""
:constant int THRESHOLD_UNIQUE_MULTIPLE_CHOICE: Threshold used to identify multiple choice questions from closed ones
"""
THRESHOLD_UNIQUE_MULTIPLE_CHOICE = 10
