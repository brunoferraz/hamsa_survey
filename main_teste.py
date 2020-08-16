import hamsa as hs
# from hamsa import question
ds = hs.read_csv("data/fofoca_ajustado.csv", token=";")


# ds.list_questions[5].getQuestion()
print(ds.getQuestion(7))
# ds = hs.read_csv("data/encoded.csv")
# print(ds)
# # import sys
# # print(sys.path)

# help(__builtins__)