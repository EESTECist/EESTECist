from django.views import generic
from django.shortcuts import render
from raffle.models import Entry

class IndexView(generic.ListView):
    model = Entry


def privacy(request):
    return render(request, "privacypolicy.htm")
