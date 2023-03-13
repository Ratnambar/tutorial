from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import FeedbackForm


def get_name(request): 
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, "templates/success.html")
    form = FeedbackForm()
    return render(request, "feedback/base.html", {"form":form})
            
