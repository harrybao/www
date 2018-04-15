# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import School,Questions
from django.db import connection
from django import forms
import json

def main(req):
    return render(req,'home/main.html')


def api(req):
	return HttpResponse("Is Json")


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
