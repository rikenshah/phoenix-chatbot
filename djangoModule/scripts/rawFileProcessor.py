import pprint, re
from nltk.corpus import stopwords
from collections import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

class rawFileProcessor(object):
    def __init__(self):
        pass

    def dict_create(self):
        text_file = open("data/sample.txt", "r")
        lines = text_file.read()
        # print lines
        questions = [] #creating an empty questions lists which will store questions
        answers = [] #creating an empty answers lists which will store answers
        splitted = lines.split(';;') #splitting of the knowledge base
        knowledgeBase = {}

        print splitted

        for line in splitted:
            separateQA = line.split('___') #separating the question and answers
            stripped_list = map(lambda s: s.strip(), separateQA) #create 2 sepate lists for purpose of dictionary creation
        # print stripped_list
            if len(stripped_list) != 2:
                print "No list"
            else:
                temp = stripped_list[0].replace('\n','').replace("?","")
                questions.append(temp)
                answers.append(stripped_list[1])

        # print knowledgeBase
        # print questions
        # print answers

        knowledgeBase = dict(zip(questions, answers))

        # pprint.pprint(knowledgeBase)
        return knowledgeBase

    def extract_keywords(self,query):
    	# query = "Register me for the event"
        word_list = word_tokenize(query.lower())

        question_map = {
	    'when' : 'time',
	    'where' : 'place',
	    'who' : 'person',
	    'venue' : 'place',
	    'me' : 'person',
        'many' : 'number',
        }

        # Apply question map
        for index,word in enumerate(word_list):
	        if word in question_map:
		        word_list[index] = question_map[word]

        # Remove stop_words from word_list
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]
        # print filtered_words

        # Stemming using porter stemmer
        ps = PorterStemmer()
        stem_words = [ ps.stem(word) for word in filtered_words]
        # print stem_words
        return stem_words