import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("song data.csv")

# Select features
features = data[['acousticness','danceability','energy','instrumentalness',
                 'liveness','loudness','speechiness','tempo','valence']]

# Scale features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)

# Create similarity matrix
similarity = cosine_similarity(scaled_data)

# Save files using pickle
pickle.dump(similarity, open('similarity.pkl','wb'))
pickle.dump(data, open('songs.pkl','wb'))

print("Model saved successfully!")