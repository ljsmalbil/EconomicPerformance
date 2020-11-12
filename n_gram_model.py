# Code based on https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/
import bs4 as bs
import urllib.request
import ssl
import random
import nltk

import re
ssl._create_default_https_context = ssl._create_unverified_context

#raw_html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Tennis')
raw_html = urllib.request.urlopen('https://nl.wikipedia.org/wiki/Economie_van_Nederland')

raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')
article_paragraphs = article_html.find_all('p')
article_text = ''

for para in article_paragraphs:
    article_text += para.text

article_text = article_text.lower()


article_text = re.sub(r'[^A-Za-z. ]', '', article_text)
print(article_text)


ngrams = {}
words = 3

words_tokens = nltk.word_tokenize(article_text)
for i in range(len(words_tokens)-words):
    seq = ' '.join(words_tokens[i:i+words])
    print(seq)
    if  seq not in ngrams.keys():
        ngrams[seq] = []
    ngrams[seq].append(words_tokens[i+words])


curr_sequence = ' '.join(words_tokens[0:words])
output = curr_sequence
for i in range(100):
    if curr_sequence not in ngrams.keys():
        break
    possible_words = ngrams[curr_sequence]
    print(possible_words)
    print('pw')
    next_word = possible_words[random.randrange(len(possible_words))]
    output += ' ' + next_word
    seq_words = nltk.word_tokenize(output)
    curr_sequence = ' '.join(seq_words[len(seq_words)-words:len(seq_words)])

print(output)

print('check')

print(curr_sequence)


