import nltk
from nltk.tokenize import word_tokenize
import random


nltk.data.path.append('/home/henry/nltk_data')  


intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "farewell": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thanks", "thank you", "thx"],
}


responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "unknown": ["I don't understand.", "Can you say that differently?", "Sorry, I didn't get that."],
}


def classify_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for intent, keywords in intents.items():
        if any(word in tokens for word in keywords):
            return intent
    return "unknown"


def chatbot():
    print("Chatbot is running! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Bye!")
            break
        intent = classify_intent(user_input)
        print("Chatbot:", random.choice(responses[intent]))


if __name__ == "__main__":
    chatbot()
