import pandas as pd

data = pd.read_csv('saves/2.cleaned_transcripts_df.csv', index_col = 0)
data


# Imports
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Vectorize
vectorizer = CountVectorizer(stop_words = 'english')
vectorized_data = vectorizer.fit_transform(data['Transcript'])

# Convert to DataFrame
vectorized_df = pd.DataFrame(vectorized_data.toarray(), columns = vectorizer.get_feature_names())
vectorized_df.index = data.index
vectorized_df


vectorized_df.to_csv('saves/3.vectorized_transcripts_df.csv')


vectorized_df = vectorized_df.transpose()


top_words = {}

for column in vectorized_df.columns:
    tokens = vectorized_df[column]
    tokens = tokens.sort_values(ascending = False).head(30)    
    
    top_words[column] = tokens
    print(column + ':\n -', ', '.join(list(tokens.index[:15])))


top_all_words = []

for column in vectorized_df.columns:
    words = list(top_words[column].index)
    
    for word in words: top_all_words.append(word)


# Imports
from collections import Counter

# Find words that are common between atleast 6 of the comedians
add_stop_words = [word for word, count in Counter(top_all_words).most_common() if count > 6]
add_stop_words


clean_df = pd.read_csv('saves/2.cleaned_transcripts_df.csv', index_col = 0)
clean_df


# Imports
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer

# Update the stop words list
stop_words = text.ENGLISH_STOP_WORDS.union(add_stop_words)


vectorizer = CountVectorizer(stop_words = stop_words)
data_cv = vectorizer.fit_transform(clean_df['Transcript'])
new_vectorized_df = pd.DataFrame(data_cv.toarray(), columns = vectorizer.get_feature_names())
new_vectorized_df.index = clean_df.index


new_vectorized_df.to_csv('saves/3.stopwords_vectorized_df.csv')


# Imports
from wordcloud import WordCloud

wc = WordCloud(
    stopwords = stop_words,
    background_color = "white",
    colormap = "Dark2",
    max_font_size = 150,
    random_state = 42
)


# Imports
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16, 6]

# Create subplots for each comedian
for index, comedian in enumerate(clean_df.index):
    wc.generate(clean_df['Transcript'][index])
    
    plt.subplot(3, 4, index + 1)
    plt.imshow(wc, interpolation = "bilinear")
    plt.axis("off")
    plt.title(comedian)

plt.show()












