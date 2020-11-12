# Code based on https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/
import bs4 as bs
import urllib.request
import ssl
import random
import nltk

import re
ssl._create_default_https_context = ssl._create_unverified_context

from data_loader import LoadData


article_list =['Economie_van_Nederland', 'Geschiedenis_van_Nederland'] #  #'Economie_(systeem)', 'Bruto_nationaal_product', 'Bruto_binnenlands_product', 'Aandelenindex']

object = LoadData(string_list=article_list)
article_text = object.return_data()

ngrams = {}
words = 4

words_tokens = nltk.word_tokenize(article_text)
for i in range(len(words_tokens)-words):
    seq = ' '.join(words_tokens[i:i+words])
    #print(seq)
    if  seq not in ngrams.keys():
        ngrams[seq] = []
    ngrams[seq].append(words_tokens[i+words])

curr_sequence = ' '.join(words_tokens[0:words])
output = curr_sequence
for i in range(100):
    if curr_sequence not in ngrams.keys():
        break
    possible_words = ngrams[curr_sequence]
    next_word = possible_words[random.randrange(len(possible_words))]
    output += ' ' + next_word
    seq_words = nltk.word_tokenize(output)
    curr_sequence = ' '.join(seq_words[len(seq_words)-words:len(seq_words)])

print(output)

print('check')

#print(curr_sequence)
