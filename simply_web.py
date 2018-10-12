from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from textrank4zh import TextRank4Sentence


class Frame(webdriver.Chrome):
    """docstring for Frame"""

    def __init__(self):
        path = '/Users/lhm/chromedriver'
        options = Options()
        options.add_argument('--headless')
        super(Frame, self).__init__(path, chrome_options=options)


def get_text(html):
    soup = BeautifulSoup(html, 'html5lib')
    target_tag = soup.find('span', class_='label', text='html')
    final_tag = target_tag.parent.parent
    result = final_tag.getText()
    return result


def get_html(url):
    url_root = 'https://www.diffbot.com/testdrive/?api=article&url='
    url_final = url_root + url
    driver = Frame()
    print('reading url...')
    driver.get(url_final)
    html = driver.page_source
    print('readed')
    driver.quit()
    return html


def analyze_text(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    for i in tr4s.get_key_sentences():
        print(i.index, i.weight, i.sentence)


def test(url):
    html = get_html(url)
    text = get_text(html)
    analyze_text(text)
    return 0
