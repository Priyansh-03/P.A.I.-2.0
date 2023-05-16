import random

# Define book recommendations for different moods
book_recommendations = {
    'happy': ['The Alchemist by Paulo Coelho', 'Harry Potter series by J.K. Rowling', 'Pride and Prejudice by Jane Austen'],
    'sad': ['The Kite Runner by Khaled Hosseini', 'The Book Thief by Markus Zusak', 'A Little Life by Hanya Yanagihara'],
    'adventurous': ['The Hobbit by J.R.R. Tolkien', 'Treasure Island by Robert Louis Stevenson', 'Into the Wild by Jon Krakauer'],
    'romantic': ['Romeo and Juliet by William Shakespeare', 'The Notebook by Nicholas Sparks', 'Jane Eyre by Charlotte Brontë']
}

# Function to recommend a book based on mood
def recommend_book(mood):
    if mood in book_recommendations:
        books = book_recommendations[mood]
        recommended_book = random.choice(books)
        return recommended_book
    else:
        return "Sorry, I don't have any recommendations for that mood."

# Main program
if __name__ == '__main__':
    # Prompt the user for their mood
    user_mood = input("Enter your mood (happy, sad, adventurous, romantic): ")

    # Recommend a book based on the user's mood
    recommended_book = recommend_book(user_mood.lower())

    # Display the recommended book
    print("Recommended book for", user_mood, "mood:", recommended_book)