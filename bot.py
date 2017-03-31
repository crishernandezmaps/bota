#!/usr/bin/python3
import pandas as pd
from textblob import TextBlob

# Get texts from timeline
#texts = pd.read_csv('texts.csv', header = None)
texts = pd.read_csv('texts.csv', header = None, encoding = 'utf8')

# iterates over texts and return the text on each row
l = []
for index, row in texts.itertuples():
    # Split sentences by '.'
    blob = TextBlob(row)
    for sentence in blob.sentences:
        # Return sentences less than 140 characters
        if len(sentence) <= 140:
            f = {'frase':sentence,'caracteres':len(sentence)}
            l.append(f)
            print(f)

df = pd.DataFrame(l)
dfi = df.set_index('caracteres')
dfi.to_csv('frases.csv', sep=',', encoding='utf-8')
print('Done!')


# df.to_csv('results.csv', sep='\t', encoding='utf-8')

#######################
# Thing to do:
# 1.- Wirte better the script or Call 'timeline.csv' and if the row is splited create tweets on a thread.
# 2.- Add image to tweet
# 3.- Add images to tweets without images
# 4.- Add context to tweet (bot posting to wordpress? > Deploybot)

'''
NOTE: for python2 use
#!/usr/bin/env
... on terminal
'''
