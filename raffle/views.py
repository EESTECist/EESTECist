from django.views import generic
from django.shortcuts import render, HttpResponse
from raffle.models import Entry


def IndexView(request):
    return HttpResponse("<h1>Raffle</h1>")


def participants(request):
    return render(request, "participants.html")


def privacy(request):
    return render(request, "privacypolicy.htm")
