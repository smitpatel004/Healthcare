
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Tweet(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     text=models.TextField(max_length=240)
#     photo=models.ImageField(upload_to='photos/',blank=True,null=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f'{self.user.username}-{self.text[:10]}'


# class Quiz(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     text=models.TextField(max_length=240)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f'{self.user.username}-{self.text[:10]}'


# Create your models here.
class Person(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    chat=models.JSONField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username}-{self.text[:10]}'
from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the built-in User model

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Tracks which user the chat belongs to
    chat_data = models.JSONField(default=list)  # Stores the chat history as a JSON list
    created_at = models.DateTimeField(auto_now_add=True)  # Optional: for tracking when the chat was created

    def __str__(self):
        return f"Chat for {self.user.username} at {self.created_at}"
    

