
import pandas as pd

r = pd.read_csv('input/question-2/main.csv')
min_age =r.groupby('occupation').agg({'age':['min','max']})

print(min_age)

min_age.to_csv('output/answer-2/answer.csv')