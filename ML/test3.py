from bots import LatinSuperBot
import pandas as pd

df = pd.read_csv('datasets/wordstuff2.csv')

X_test = list(df['words'])
y_test = list(df['descriptions'])


predictions = []

bot = LatinSuperBot('levenshtein')

for value in X_test:
    results = bot.run(value)
    predictions.append(results)


accurate = 0
total = 0

for i, x in enumerate(y_test):
    for value in predictions:
        if x in value: 
            accurate += 1
            break
        else:
            print(x)
            print('not in')
            print(value)
    total += 1
    print(f'Total: {total}')
    print(f'Total accurate: {accurate}')
    print(f'Accuracy: {accurate/total}')



    


