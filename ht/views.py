from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(req):
    return render(req,'ht/index.html')

def login(req):
    return render(req,'ht/login.html')

def add(req):
    return render(req,'ht/add.html')

def adv(req):
    return render(req,'ht/adv.html')

def book(req):
    return render(req,'ht/book.html')

def cate(req):
    return render(req,'ht/cate.html')

def catedit(req):
    return render(req,'ht/catedit.html')

def column(req):
    return render(req,'ht/column.html')

def info(req):
    return render(req,'ht/info.html')

def list(req):
    return render(req,'ht/list.html')

def page(req):
    return render(req,'ht/page.html')

def pas(req):
    return render(req,'ht/pas.html')

def tips(req):
    return render(req,'ht/tips.html')
