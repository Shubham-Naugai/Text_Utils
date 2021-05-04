# my file = Shubham Naugai
from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text input
    yourtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    if removepunc == 'on':
        # analyze the text
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzedtext = ""
        for char in yourtext:
            if char not in punctuations:
                analyzedtext = analyzedtext + char
        punc = {'purpose': 'Opperation SuccessFull', 'analyzed_text': analyzedtext}
        yourtext = analyzedtext
    if fullcaps == 'on':
        analyzedtext = ""
        for char in yourtext:
            analyzedtext = analyzedtext + char.upper()
        punc = {'purpose': 'Opperation SuccessFull', 'analyzed_text': analyzedtext}

    if removepunc != 'on' and fullcaps != 'on':
        return  HttpResponse('ERR: Plese select any operation!')
    return render(request, 'analyze.html', punc)

def Presonal_Navigator(request):
    pn = '''<h1>Frequently used Websites by Shubham Naugai</h1><br>
    <a href = "https://www.w3schools.com/"> W3schools for any reference </a><br>
    <a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django lectures </a><br>
    <a href = "https://docs.djangoproject.com/en/3.2/intro/"> Django official documentation </a><br>
    <a href = "https://www.google.com/"> Google </a><br>
    <a href = "https://www.geeksforgeeks.org/"> GeeksForGeeks </a><br>
    <a href = "/"> Back </a><br>'''
    return HttpResponse(pn)

