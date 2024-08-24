from django import forms

class Articleform(forms.form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()