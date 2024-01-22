## TV Show Recommendation Application

This code provides a recommendation system based on content-based filtering using the user-item matrix. It predicts ratings for anime shows and generates personalized recommendations for users.

### Prerequisites
- Python 3.x
- pandas
- scikit-learn
- NumPy
- FuzzyWuzzy
- Streamlit


### Data
The code assumes the presence of the following CSV file in the current working directory:

- `anime.csv`: Contains information about anime shows, including anime_id, name, genre, type, episodes, rating, and members.

### Instructions for Use
1.  Ensure that the required CSV file `anime.csv` are present in the same directory as the Python script
2.  Run the code ensuring that 2 pickle files (`animes_list.pkl` and `similarity.pkl`) are generated
3.  In the terminal, enter the command `streamlit run app.py`
4.  Enter the desired anime title into the search box located in the application window to receive the top 5 personalized recommendations for similar anime titles.
    - Click on the poster titles to be redirected to a page for more information on that title


https://github.com/AlexIbasitas/AnimeMatch/assets/77213807/d1ede859-2f18-4d9b-8cca-0e9550300549

