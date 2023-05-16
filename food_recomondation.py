import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data for food recommendations
food_data = {
    'food_name': ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Tacos'],
    'mood': ['happy', 'happy', 'adventurous', 'comforting', 'adventurous'],
    'time': ['dinner', 'lunch', 'dinner', 'dinner', 'lunch']
}

# Function to recommend food based on mood
def recommend_food_by_mood(user_mood):
    df = pd.DataFrame(food_data)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['mood'])
    mood_similarities = cosine_similarity(tfidf_matrix, vectorizer.transform([user_mood]))
    sorted_indices = mood_similarities.argsort(axis=0)[::-1].flatten()
    sorted_food = df['food_name'].iloc[sorted_indices]
    return sorted_food.values.tolist()

# Function to recommend food based on time
def recommend_food_by_time(current_time):
    df = pd.DataFrame(food_data)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['time'])
    time_similarities = cosine_similarity(tfidf_matrix, vectorizer.transform([current_time]))
    sorted_indices = time_similarities.argsort(axis=0)[::-1].flatten()
    sorted_food = df['food_name'].iloc[sorted_indices]
    return sorted_food.values.tolist()

# Main program
if __name__ == '__main__':
    user_mood = input("Enter your mood (happy, sad, excited, etc.): ")
    current_time = datetime.datetime.now().strftime("%H:%M")

    recommended_food_by_mood = recommend_food_by_mood(user_mood)
    print("Recommended food based on mood:")
    for food in recommended_food_by_mood:
        print(food)

    recommended_food_by_time = recommend_food_by_time(current_time)
    print("Recommended food based on time:")
    for food in recommended_food_by_time:
        print(food)
