from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DocumentForm
from .models import Document
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
import os 
from os import listdir
from os.path import isfile, join

def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            if os.path.isfile('Data/sample.txt'):
            	os.remove('Data/sample.txt')


            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Get all files from Data/
            mypath = "data/"
            onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

            # Rename files[0]
            src = 'data/' + onlyfiles[0]
            os.rename(src,'data/sample.txt')
            # Redirect to the document list after POST
            return HttpResponse("Hello")
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
        documents = Document.objects.all()

    # Render list page with the documents and the form
        return render_to_response(
        'training/index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
