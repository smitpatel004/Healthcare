from django import forms
from .models import Tweet,Quiz


class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']
class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields=['text']        