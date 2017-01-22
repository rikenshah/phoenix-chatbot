from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DocumentForm
from training.models import Document, KnowledgeBase
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
import os, sys, pickle
from os import listdir
from os.path import isfile, join
from scripts import rawFileProcessor
from django.forms.models import model_to_dict

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

            rp = rawFileProcessor.rawFileProcessor()
            model_dict = {}
            model_dict = rp.dict_create()

            cleanedKnowledgeBase = {}
            index = 0
            for key,value in model_dict.iteritems():
                temp = rp.extract_keywords(key)
                cleanedKnowledgeBase[index] = {
                    'keywords' : '_'.join(temp),
                    'answer' : value
                }
                index = index + 1;

            print "++++++++++++"
            print cleanedKnowledgeBase

            with open("data/pickleDumps/kn.pickle", "wb") as output_file:
                pickle.dump(cleanedKnowledgeBase, output_file)

            # with open("someobject.pickle", "rb") as input_file:
            #     e = Pickle.load(input_file)

            # print "mdoel dict"
            # print model_dict
            for key, value in model_dict.iteritems():
                
                q = KnowledgeBase(question = key, answers = value)
                q.save()
                # print q.question
    
            # kb = KnowledgeBase()
            # print KnowledgeBase.objects.get(question="What is the time of the hackathon?")
            # Redirect to the document list after POST
            return HttpResponse("Hello")
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
        documents = Document.objects.all()

    # Render list page with the documents and the form
        return render(request,'training/index.html',{'documents': documents, 'form': form})
