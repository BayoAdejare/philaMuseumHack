import json
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello! You are at the Philadelphia Museum Hack iBeacons")

def import_beacons(request):
    f = open('PMAPowerofArtHackathon-ibeacons.json', 'r')
    data = json.load(f)
    assert isinstance(data, object)
    return data
