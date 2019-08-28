from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   text = """<h1>ML with Scikit Learn - Linear Regression Demo</h1>"""
   return HttpResponse(text)