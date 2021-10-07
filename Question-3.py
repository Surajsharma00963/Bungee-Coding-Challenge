import pandas as pd

#reading a csv file
r = pd.read_csv('input/question-3/main.csv')

sort=r.sort_values(by=['Red Cards','Yellow Cards'],ascending=False)[['Team','Yellow Cards','Red Cards']]

print(sort)

sort.to_csv('output/answer-3/answer.csv')