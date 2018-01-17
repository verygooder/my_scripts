from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from bs4 import BeautifulSoup
from sys import argv
import re
import os
import time


def get_tags(url):
    # read url, get soup, extract img tags in the url
    print('reading ' + url)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    print('reading complete')
    soup = BeautifulSoup(html, 'html5lib')
    tag_lst = soup.find_all('li')
    tag_lst = [i for i in tag_lst if i.get(
        'id') is not None and i.get('id').startswith('comment')]
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
        def vote_format(x): return int(x[1:-1])
        self.like = vote_format(self.vote_lst[0])
        self.unlike = vote_format(self.vote_lst[1])
        self.rate = self.like / (self.like + self.unlike) * 100
        self.rate = round(self.rate, 2)
        # self.target = True if self.rate > 90 else False

    def __repr__(self):
        return self.id


def give_driver():
    # return a selenium webdriver obj
    with open('./setting', 'r') as f:
        data = f.read()
    import_dic = json.loads(data)
    header = DesiredCapabilities.PHANTOMJS
    header['phantomjs.page.settings.userAgent'] = import_dic['User-Agent']
    path = import_dic[os.name]
    driver = webdriver.PhantomJS(path, desired_capabilities=header)
    return driver


driver = give_driver()
page_start = int(argv[1])
page_end = int(argv[2])
# url format 'http://jandan.net/ooxx/page-482#comments'
url_head = 'http://jandan.net/ooxx/page-'
url_tail = '#comments'
url_lst = [url_head +
           str(i) + url_tail for i in range(page_start, page_end + 1)]
tag_lst = []
for url in url_lst:
    tags = get_tags(url)
    tag_lst += tags
driver.quit()
comments = [Comment(i) for i in tag_lst]
# comments_ok = [i for i in comments if i.target]
comments_info_string = [
    '\t'.join([str(i.rate), i.url, i.id]) for i in comments]
with open('./result.tsv', 'w') as f:
    for i in comments_info_string:
        f.writelines(i + '\n')
