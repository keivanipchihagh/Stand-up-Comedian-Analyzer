# Imports
import pickle

transcripts = []
with open('saves/transcripts_data.json', 'rb') as file:
    transcripts = pickle.load(file)


for comedian in transcripts:
    transcripts[comedian] = [' '.join(transcripts[comedian]).lower()]


# Imports
import pandas as pd

data = pd.DataFrame.from_dict(transcripts).transpose()
data.columns = ['Transcript']
data.head()


# Imports
import re
import string

def clean_data(text):
    ''' Phase 1 '''
    
    text = re.sub('\[.*?\]', '', text)                                 # Texts in brackets
    text = re.sub('\w*\d\w*', '', text)                                # Numbers
    text = re.sub('[get_ipython().run_line_magic("s]'", " % re.escape(string.punctuation), '', text)    # Punctuations")
    text = re.sub('\n', ' ', text)                                     # \n
    text = re.sub('[“”–]', '', text)                                   # More punctuations
    text = text.strip()                                                # Strip
    
    return text
    
cleaned_data = pd.DataFrame(data['Transcript'].apply(lambda x: clean_data(x)))
cleaned_data['Transcript'][0]


import spacy

nlp = spacy.load('en_core_web_sm')

def lemmatize(text):
    text = re.sub('’', '\'', text)    # Spacy doesn't understand '’'!
    
    return ' '.join([token.lemma_ for token in nlp(text)])

lemmatized_data = pd.DataFrame(cleaned_data['Transcript'].apply(lambda x: lemmatize(x)))
lemmatized_data['Transcript'][0]


def fill_data(text):
    ''' Phase 2 '''
    
    text = re.sub('’em', ' them ', text)
    text = re.sub(' ’ ', ' is ', text)
    text = re.sub('’re', ' are ', text)
    text = re.sub('n’t', 'not', text)
    
    return text
    
filled_data = pd.DataFrame(lemmatized_data['Transcript'].apply(lambda x: fill_data(x)))
filled_data['Transcript'][0]


filled_data.to_csv('saves/cleaned_transcripts_df.csv')
