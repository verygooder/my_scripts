from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import sys
from readability import Document
from bs4 import BeautifulSoup
import re
from textrank4zh import TextRank4Sentence


class Frame(webdriver.Chrome):
    """docstring for Frame"""

    def __init__(self):
        path = '/Users/lhm/chromedriver'
        options = Options()
        # options.add_argument('--headless')
        super(Frame, self).__init__(path, chrome_options=options)
        self.set_page_load_timeout(20)


def get_html(url):
    f = Frame()
    try:
        f.get(url)
        html = f.page_source
        f.quit()
    except TimeoutException:
        print('connection timeout')
        f.quit()
        sys.exit()
    return html


def html_simplify(html):
    doc = Document(html)
    simple = doc.summary()
    soup = BeautifulSoup(simple, 'html5lib')
    text = soup.getText()
    text = strip_text(text)
    return text


def strip_text(text):
    text = re.sub(' ', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\t', '', text)
    return text


def text_abstract(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text)
    sentences_count = len(tr4s.sentences) // 4
    if sentences_count <= 6:
        sentences_num = sentences_count
    else:
        sentences_num = 6
    abstract_sentences = tr4s.get_key_sentences(num=sentences_num)
    abstract_sentences.sort(key=lambda x: x['index'])
    return abstract_sentences


def test(url):
    html = get_html(url)
    text = html_simplify(html)
    sentences = text_abstract(text)
    for i in sentences:
        print(i['sentence'] + '\n')
    return 0


