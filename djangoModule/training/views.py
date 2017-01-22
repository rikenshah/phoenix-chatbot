from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrainingForm

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = TrainingForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			analysisData = {}
			inputText = form.data['inputText']
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'training/analysis.html', {'data': analysisData ,'title': "Full Analysis"})


	# if a GET (or any other method) we'll create a blank form
	else:
		form = TrainingForm()

	return render(request, 'training/index.html', {'form': form, 'title': "Input Text Para"})