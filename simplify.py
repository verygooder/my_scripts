import requests
from bs4 import BeautifulSoup
from sys import exit
from textrank4zh import TextRank4Sentence
import re


def get_string(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        html = r.text
    else:
        print('cant connect')
        exit()
    soup = BeautifulSoup(html, 'html5lib')
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('style')]
    result = soup.getText(strip=True)
    return result


def analyze_url(url):
    string = get_string(url)
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=string, lower=True, source='all_filters')
    for i in tr4s.get_key_sentences(num=7):
        print(i.sentence)