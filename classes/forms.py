from django import forms
from .models import Club, Student
from django.contrib.auth.models import User

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['club_name', 'club_logo']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_age', 'stream','cover']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username', 'password']