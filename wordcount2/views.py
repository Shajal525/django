from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	words = fulltext.split()
	dictionary = {}
	for word in words:
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1
	
	listdictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext':fulltext, 'wordsdictionary':listdictionary, 'count':len(words)})

def about(request):
	return render(request, 'about.html')