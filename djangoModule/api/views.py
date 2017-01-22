from django.shortcuts import render
from django.http import HttpResponse
from scripts import rawFileProcessor
import pickle
from django.http import JsonResponse

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'GET':

		# print request.data
		query = request.GET.get('query')
		print query

		rp = rawFileProcessor.rawFileProcessor()
		query_keywords = rp.extract_keywords(query)

		with open("data/pickleDumps/kn.pickle", "rb") as input_file:
			c = pickle.load(input_file)

		print c
		for key,value in c.iteritems():
			print value['keywords']

		# return json response
		return JsonResponse({'answer' : 'invalid request'})



	# if a GET (or any other method) we'll create a blank form
	else:
		return JsonResponse({'answer' : 'invalid request'})

	return render(request, 'training/index.html', {'form': form, 'title': "Input Text Para"})