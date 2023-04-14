from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import Student

class Form(ModelForm):
    class Meta:
        model = Student
        exclude = ['created_at']


def tutorial(request):
    form = Form()
    return render(request, 'tutorial.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')


def webdev(request):
    return render(request, 'webdev.html')


def ai_ml(request):
    return render(request, 'ai_ml.html')


def basic_coding(request):
    return render(request, 'basic_coding.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def submit_form(request):
    form = Form(request.POST)
    form.save()
    return redirect('thank_you')
