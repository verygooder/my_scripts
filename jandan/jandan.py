from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from bs4 import BeautifulSoup
from sys import argv
import re
import os


def get_tags(url):
    print('reading ' + url)
    driver.get(url)
    html = driver.page_source
    print('reading complete')
    soup = BeautifulSoup(html, 'html5lib')
    tag_lst = soup.find_all('li')
    tag_lst = [i for i in tag_lst if i.get('id') is not None and i.get('id').startswith('comment')]
    return tag_lst


class Comment(object):
    """docstring for Comment"""

    def __init__(self, tag):
        super(Comment, self).__init__()
        self.tag = tag
        self.href = self.tag.find('a', class_='view_img_link')['href']
        self.url = 'http:' + self.href
        self.id = self.tag.get('id')
        self.vote_lst = re.findall(r'\[\d.*?\]', tag.get_text())
        vote_format = lambda x: int(x[1:-1])
        self.like = vote_format(self.vote_lst[0])
        self.unlike = vote_format(self.vote_lst[1])
        self.rate = self.like / (self.like + self.unlike) * 100
        self.rate = round(self.rate, 2)


page_start = int(argv[1])
page_end = int(argv[2])
# url format 'http://jandan.net/ooxx/page-482#comments'
url_head = 'http://jandan.net/ooxx/page-'
url_tail = '#comments'
url_lst = [url_head + str(i) + url_tail for i in range(page_start, page_end + 1)]
with open('./setting', 'r') as f:
    data = f.read()
import_dic = json.loads(data)
header = DesiredCapabilities.PHANTOMJS
header['phantomjs.page.settings.userAgent'] = import_dic['User-Agent']
path = import_dic[os.name]
driver = webdriver.PhantomJS(path, desired_capabilities=header)

