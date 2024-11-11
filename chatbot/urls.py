from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.chatbot_view, name='chatbot'),
#     path('get-response/', views.chat_response, name='chat_response'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),  # Renders the chatbot page
    path('chatbot/get-response/', views.chat_response, name='chat_response'),  # Handles chat responses
]
