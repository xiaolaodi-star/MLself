from MachineLearning.FAQsystem.startjieba import startjieba
from MachineLearning.FAQsystem.system import system

a=system()
a.sentense_get()
a.limit_low_words(1)
a.word_tfidf()
# print(a.system_ES)
# print(a.alldoc,a.allword)
# print(a.system_tfidf)
for i in range(10):
    question=input("请输入问题：")
    a.userquestion(question)
    input("pause to continue...")
