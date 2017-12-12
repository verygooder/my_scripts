# coding=utf-8
import re
import requests
from bs4 import BeautifulSoup


class Book(object):
    """docstring for Book"""

    def __init__(self, soup):
        super(Book, self).__init__()
        self.soup = soup
        self.link = self.get_link()
        self.author = self.get_author()
        self.score = self.get_score()
        self.name = self.get_book_name()

    def __repr__(self):
        return self.name

    def get_rid(self, string):
        partten1 = r'\n'
        partten2 = r'\ {2}'
        result = re.sub(partten1, '', string)
        result = re.sub(partten2, '', result)
        return result

    def get_link(self):
        tail = self.soup.a['href']
        link = 'http://readfree.me' + tail
        return link

    def get_score(self):
        tmp = self.soup.find_all('span', class_='badge badge-success')[0]
        score = tmp.get_text()
        score = self.get_rid(score)
        score = 0.0 if score == 'DIY' else score
        return score

    def get_book_name(self):
        tmp = self.soup.div(class_='book-info')[0]
        book_name = tmp.a.get_text()
        book_name = self.get_rid(book_name)
        return book_name

    def get_author(self):
        tmp = self.soup.div(class_='book-author')[0]
        author = tmp.get_text()
        author = self.get_rid(author)
        return author

    def print_of(self):
        out_lst = [
            self.score,
            self.name,
            self.author,
            self.link
        ]
        out_lst_format = [str(i) for i in out_lst]
        string = ' '.join(out_lst_format)
        return string


def get_soup(url='http://readfree.me'):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'sessionid=6dpp4wx0d8f79dgriva0hjb9py7011cx; Hm_lvt_375aa6d601368176e50751c1c6bf0e82=1500264101,1501478607; Hm_lpvt_375aa6d601368176e50751c1c6bf0e82=1501478990; csrftoken=jEboOF25CANnkHdQAfpdh2E4U7ivLE2ywnp1CFbGwJlUTIiWk9HQ3ea311AJLGvR',
        'DNT': '1',
        'Host': 'readfree.me',
        'Referer': 'http://readfree.me/accounts/login/?next=/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup


def extract_books(soup):
    lst = soup.find_all('li', class_='book-item')
    return lst


if __name__ == '__main__':
    root_url = 'http://readfree.me/?page='
    url_lst = [root_url + str(i) for i in range(1, 6)]
    soup_lst = [get_soup(i) for i in url_lst]
    soup_extracts = [extract_books(i) for i in soup_lst]
    all_soup = [i for x in soup_extracts for i in x]
    books = [Book(i) for i in all_soup]
    books = sorted(books, key=lambda x: float(x.score), reverse=False)
    for book in books:
        print(book.print_of())





