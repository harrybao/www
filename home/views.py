from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(req):
    return render(req,'home/main.html')
def api(req):
    return HttpResponse("I like Python")
