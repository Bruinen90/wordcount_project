import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    fulltextlow = fulltext.lower()
    wordslist = fulltextlow.split()
    worddict = {}
    for word in wordslist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    wordssorted = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordslist), 'worddict': wordssorted})

def about(request):
    return render(request, 'about.html')