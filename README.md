## TV Show Recommendation Application

This code provides a recommendation system based on collaborative filtering using the user-item matrix. It predicts ratings for anime shows and generates personalized recommendations for users.

Prerequisites
Python 3.x
Pandas
NumPy
scikit-learn
Data
The code assumes the presence of the following CSV files in the current working directory:

anime.csv: Contains information about anime shows, including anime_id, name, genre, type, episodes, rating, and members.
rating.csv: Contains user ratings for anime shows, including user_id, anime_id, and rating.
