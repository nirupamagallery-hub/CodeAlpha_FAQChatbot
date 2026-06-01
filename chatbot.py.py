import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
data = pd.read_csv("faq.csv")

questions = data["Question"]
answers = data["Answer"]

# Convert questions into vectors
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)

print("FAQ Chatbot is Ready!")
print("Type 'exit' to stop.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Convert user question into vector
    user_vector = vectorizer.transform([user_input])

    # Compare similarity
    similarity = cosine_similarity(user_vector, question_vectors)

    # Find best matching question
    index = similarity.argmax()

    # Display answer
    print("Bot:", answers[index])