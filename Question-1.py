import pandas as pd

#reading a csv file
r = pd.read_csv('input/question-1/main.csv')

# taking maximum population in the particular year
maximum_population = r.groupby([(r.Year//10)*10])[['Population']].max()


attributes_mean = r.groupby([(r.Year//10)*10])[['Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']].mean()

final = maximum_population.join(attributes_mean)

print(final)

final.to_csv('output/answer-1/answer.csv')




