from django.shortcuts import render
from django.http import HttpResponse

from .models import Push
from .serializers import PushSerializer


from rest_framework import viewsets

class PushViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Push.objects.all().order_by('-when')
    serializer_class = PushSerializer


def index(request):
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
