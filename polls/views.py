from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.all()
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})