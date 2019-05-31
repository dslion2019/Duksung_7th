from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ['title', 'name', 'role', 'body']
        labels = {
            "title" : "카테고리",
            "name" : "이름",
            "role" : "역할",
            "body" : "후기"
        }