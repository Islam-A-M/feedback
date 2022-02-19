from dataclasses import fields
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Review
# standard way

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name' , max_length=100, min_length=4, error_messages={
#         "required":"Your name must not be empty",
#         "max_length":"Please enter a shorter name!",
#          "min_length":"Please enter a shorter name!",

#     })
    
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200, )
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewFormViewOnly(forms.Form):
    user_name = forms.CharField(label='Your Name' ,disabled=True)
    
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200,disabled=True )
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5,disabled=True)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
      # fields = ['user_name', 'rating', 'review_text'] #or __all__
        fields = '__all__'
       # exclude = ['rating']
        labels = {
           "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating",
        }
        error_messages= {
           "user_name":{
           "required":"Your name must not be empty",
      "max_length":"Please enter a shorter name!",
          "min_length":"Please enter a shorter name!",

               },

            
        }