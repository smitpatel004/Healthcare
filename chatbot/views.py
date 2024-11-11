import random
import json
import pickle
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from tensorflow.keras.models import load_model
import os
from .models import Person,Chat

# Load the model and data (ensure correct path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = load_model(os.path.join(BASE_DIR, 'chatbot/model_files/chatbot_model2.h5'))

with open(os.path.join(BASE_DIR, 'chatbot/model_files/intents.json')) as file:
    intents = json.load(file)

with open(os.path.join(BASE_DIR, 'chatbot/model_files/words1.pkl'), 'rb') as file:
    words = pickle.load(file)

with open(os.path.join(BASE_DIR, 'chatbot/model_files/classes1.pkl'), 'rb') as file:
    classes = pickle.load(file)

# Helper function to preprocess user input
def preprocess_input(user_input):
    user_input = user_input.lower()
    input_data = [0] * len(words)
    for word in user_input.split():
        if word in words:
            index = words.index(word)
            input_data[index] = 1
    return np.array([input_data])

# Function to generate chatbot response
def get_response(user_input):
    input_data = preprocess_input(user_input)
    prediction = model.predict(input_data)[0]
    response_index = np.argmax(prediction)
    response_class = classes[response_index]

    for intent in intents['intents']:
        if intent['tag'] == response_class:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

# View to handle chatbot page rendering
# def chatbot_view(request):
#     return render(request, 'chat.html')
def chatbot_view(request):
    # Get the chat history for the logged-in user
    chat_history = Chat.objects.filter(user=request.user).first()  # Assuming `Chat` has a `user` field
    chat_data = chat_history.chat_data if chat_history else []  # Replace `chat_data` with the actual field storing messages
    # print(chat_data,"___________________________________________________")
    # Pass the chat history to the template
    chat_data_json = json.dumps(chat_data)

    return render(request, 'chat.html', {'chat_history': chat_data_json})
    # return render(request, 'chat.html', {'chat_history': chat_data})

# API endpoint to process user input and get chatbot response
def chat_response(request):
    user_message = request.GET.get('message', '')
    response = get_response(user_message)
    # print(user_message)
    # print("response",response)
    # sav_chat(request)
    sav_chatt(request,user_message,response)
    return JsonResponse({'response': response})

from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone

def sav_chat(request):
    print(request.user)
    print(request.user.id)
    tweet=get_object_or_404(Chat,pk=request.user.id,user=request.user)
    tweet1=Chat.objects.filter(user=request.user)
    print(tweet1)
    print(tweet)
    
    print(tweet.user)
    print(tweet.id)
    
    
    # obj=Chat.objects.get(request.user.id==id)
    print("_____________________________________________________")
    print(tweet.chat_data)
    print("_____________________________________________________")

    # obj_chat=obj.Chat
    # print(obj_chat)

def sav_chatt(request, user_message, bot_response):
    # Fetch or create a Chat object for the logged-in user
    chat, created = Chat.objects.get_or_create(user=request.user)

    # If this is the first chat, initialize chat_data as an empty list
    if created:
        chat.chat_data = []

    # Append the user's message to the chat_data
    chat.chat_data.append({
        "sender": request.user.username,  # You can use user ID or username
        "message": user_message,
        "timestamp": timezone.now().isoformat()
    })

    # Append the bot's response to the chat_data
    chat.chat_data.append({
        "sender": "bot",
        "message": bot_response,
        "timestamp": timezone.now().isoformat()
    })

    # Save the updated chat object
    chat.save()
# def chatbot_view(request):
#     chat_history = Chat.objects.filter(user=request.user).first()
#     return render(request, 'chat.html', {'chat_history': chat_history.chat_data if chat_history else []})
