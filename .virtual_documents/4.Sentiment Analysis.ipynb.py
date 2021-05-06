# Imports
import pandas as pd

vec_df = pd.read_csv('saves/3.vectorized_transcripts_df.csv', index_col = 0)
clean_df = pd.read_csv('saves/2.cleaned_transcripts_df.csv', index_col = 0)

clean_df


# Imports
from textblob import TextBlob

polarity = lambda x: TextBlob(x).sentiment.polarity
subjectivity = lambda x: TextBlob(x).sentiment.subjectivity

clean_df['Polarity'] = clean_df['Transcript'].apply(polarity)
clean_df['Subjectivity'] = clean_df['Transcript'].apply(subjectivity)

clean_df


# Imports
import matplotlib.pyplot as plt

plt.figure(figsize = (15, 5))

for index, comedian in enumerate(clean_df.index):
    x = clean_df['Polarity'].loc[comedian]
    y = clean_df['Subjectivity'].loc[comedian]
    
    plt.scatter(x, y,  c = 'b')
    plt.text(x + .001, y + .001, comedian, fontsize = 10)
    plt.xlim(-.01, .12) 

plt.title('Sentiment Analysis')
plt.xlabel('<-- Negative -------- Positive -->')
plt.ylabel('<-- Facts -------- Opinions -->')

plt.show()


num_of_splits = 10

splitted_scripts = []
for i, comedian in enumerate(clean_df.index):
    
    script = clean_df['Transcript'][comedian]
    split_len = len(script) // num_of_splits
    
    polarities = []
    subjectivities = []
    for i in range(num_of_splits):
        split = script[i * split_len: (i + 1) * split_len]
        
        polarities.append(TextBlob(split).sentiment.polarity)
        subjectivities.append(TextBlob(split).sentiment.subjectivity)
        
    splitted_scripts.append((comedian, split, polarities, subjectivities))


# Imports
import numpy as np

plt.figure(figsize = (15, 10))

for i, value in enumerate(splitted_scripts):    
    comedian, split, polarity, subjectivity = value
    
    plt.subplot(3, 4, i + 1)
    plt.plot(np.arange(0,10), polarity)
    plt.plot(np.arange(0,10), np.zeros(10))
    plt.title(comedian)
    plt.ylim(ymin = -.2, ymax = .3)
    
plt.show()









