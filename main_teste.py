import hamsa as hs
import pandas as pd
# from hamsa import question
ds = hs.read_csv("data/fofoca_ajustado.csv", token=";")

f = ds.get_questions_headings()

# temp = ds.get_questions_by_type(hs.question.QuestionType.CLOSED_MULTIPLE_CHOICE)
# temp = ds.get_questions_by_type(hs.question.QuestionType.OPENED)
# print("ABERTAS")
# for i in temp:
#     print(i.get_heading())

# temp = ds.get_questions_by_type(hs.question.QuestionType.OPENED)


# df = pd.read_csv("data/fofoca_ajustado.csv", sep=";")

# print(df.columns[4])

# ds.list_questions[5].getQuestion()
# print(ds.getQuestion(7))
# ds = hs.read_csv("data/encoded.csv")
# print(ds)
# # import sys
# # print(sys.path)

# help(__builtins__)