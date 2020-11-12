# Code based on https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/
import bs4 as bs
import urllib.request
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context

class LoadData:
    def __init__(self, string_list):
        self.string_list = string_list

    def return_data(self):
        # Get all texts as list of strings
        total_list = []
        for article in self.string_list:
            raw_html = urllib.request.urlopen('https://nl.wikipedia.org/wiki/'+article)

            raw_html = raw_html.read()

            article_html = bs.BeautifulSoup(raw_html, 'lxml')
            article_paragraphs = article_html.find_all('p')
            article_text = ''

            for para in article_paragraphs:
                article_text += para.text

            article_text = article_text.lower()
            article_text = re.sub(r'[^A-Za-z. ]', '', article_text)
            total_list.append(article_text)

        article_text = '-'.join(total_list)

        return article_text




