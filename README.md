FAQ Chatbot

Project Overview

This project is developed as part of the CodeAlpha Artificial Intelligence Internship.

The FAQ Chatbot is designed to answer frequently asked questions automatically. It uses Natural Language Processing (NLP) techniques to compare the user's question with a predefined set of FAQs and return the most relevant answer.

Features

- Interactive command-line chatbot
- Answers frequently asked questions automatically
- Uses TF-IDF Vectorization for text processing
- Uses Cosine Similarity for question matching
- Easy to customize by updating the FAQ dataset
- User-friendly interface

Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

Project Structure

FAQ Chatbot/
│
├── chatbot.py.py
├── faq.csv
└── README.md

How It Works

1. Loads FAQ data from the "faq.csv" file.
2. Extracts questions and answers from the dataset.
3. Converts questions into numerical vectors using TF-IDF.
4. Accepts a question from the user.
5. Calculates similarity between the user's question and stored FAQs.
6. Finds the most similar question.
7. Displays the corresponding answer.

Installation

Install the required libraries:

pip install pandas scikit-learn

Running the Project

Run the chatbot using:

python chatbot.py.py

Sample Interaction

FAQ Chatbot is Ready!
Type 'exit' to stop.

You: How long does shipping take?
Bot: Shipping takes 3-5 business days.

You: What is your return policy?
Bot: You can return products within 30 days.

You: exit
Bot: Goodbye!

Dataset Format

The "faq.csv" file should contain the following columns:

Question,Answer

Example:

Question,Answer
How long does shipping take?,Shipping takes 3-5 business days.
What is your return policy?,You can return products within 30 days.

Future Improvements

- Add a graphical user interface (GUI)
- Support voice input and output
- Integrate advanced NLP models
- Deploy as a web application

Author

Nirupama Pamarthi

Internship

CodeAlpha Artificial Intelligence Internship