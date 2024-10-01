# Created using phi3:mini model
# Prompt: Write a simple python app that uses streamlit to implement a chat bot.
# pip install streamlit chatbot chatterbot nltk requests pandas numpy beautifulsoup4 scikit-learn tflearn keras tensorflow==2.x tqdm flask googletrans yaspin pendulum pygments markdown unidecode python-dateutil pillow selenium webdriver_manager pyngrok

import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from selenium import webdriver
from time import sleep
import os

# Create a new instance of ChatBot named my_chatbot using the corpus loaded by training it on some data (for example, an existing conversation log)
my_chatbot = ChatBot("Sample Bot")
trainer = ListTrainer(my_chatbot)
trainer.train([
    "Hi",
    "Hello! How can I help you?",
])

st.title('Simple Python ChatBot')
# Create a text input box for the user to enter their messages (user message). The max length ensures that only one line of response is displayed at a time, keeping things simple and readable.
user_message = st.text_input("You:", key="USER")
if not user_message:
    continue  # Ensure the loop continues if no input has been given by the user yet

while True:

    try:
        response = my_chatbot.get_response(user_message)

        st.write("My Bot: " + str(response))
        sleep(1)  # Small delay to make conversation feel more natural and real-time as the bot processes user input (this line can be adjusted or removed based on actual use case needs).
    except Exception as e:
        print(e, file=sys.stderr)
        st.write("I'm sorry, I didn't understand that.")

# To run this Streamlit application using Python script execution command with '--run-python chatbot_app.py', use the following terminal commands:
# streamlit run --server.port=8090  chatbot_app.py