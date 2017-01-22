from django.shortcuts import render
from django.http import HttpResponse
from scripts import rawFileProcessor
from django.http import JsonResponse

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':

		# print request.data
		query = ""

		rp = rawFileProcessor.rawFileProcessor()
		query_keywords = rp.extract_keywords(query)

		# return json response
		


	# if a GET (or any other method) we'll create a blank form
	else:
		return JsonResponse({'answer' : 'invalid request'})

	return render(request, 'training/index.html', {'form': form, 'title': "Input Text Para"})