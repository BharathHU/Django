from django import forms
class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    place=forms.CharField()
    email=forms.EmailField()