import pandas as pd

data = pd.read_csv('saves/cleaned_transcripts_df.csv', index_col = 0)
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


vectorized_df.to_csv('saves/vectorized_transcripts_df.csv')












