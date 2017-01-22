from nltk.corpus import stopwords
from collections import OrderedDict
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

query = "Register me for the event"
word_list = word_tokenize(query.lower())

question_map = {
	'when' : 'time',
	'where' : 'place',
	'who' : 'person',
	'venue' : 'place',
	'me' : 'person'
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
print stem_words
