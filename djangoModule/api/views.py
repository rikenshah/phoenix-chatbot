from django.shortcuts import render
from django.http import HttpResponse
from scripts import rawFileProcessor
import pickle
from django.http import JsonResponse
from nltk.corpus import wordnet

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'GET':

		# print request.data
		query = request.GET.get('query')
		print "Query is_______" + query

		rp = rawFileProcessor.rawFileProcessor()
		query_keywords = rp.extract_keywords(query)

		print "query_keywords"
		print query_keywords


		with open("data/pickleDumps/kn.pickle", "rb") as input_file:
			c = pickle.load(input_file)

		print c
		maxKey = 0
		for key,value in c.iteritems():
			temp1 = value['keywords'].split("_")
			print " keywords"
			print temp1
			numCommon = len(list(set(temp1).intersection(query_keywords)))
			if numCommon>maxKey:
				maxKey = key

		print "matched keywords" + c[maxKey]['keywords']	
		answer = c[maxKey]['answer']
		print "answer is :"+answer

		# return json response
		return JsonResponse({'answer' : answer})



	# if a GET (or any other method) we'll create a blank form
	else:
		return JsonResponse({'answer' : 'invalid request'})

	return render(request, 'training/index.html', {'form': form, 'title': "Input Text Para"})