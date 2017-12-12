# This script is used to obtain and show bilibili article rank
# coding=utf-8
import requests
import json
from pycolor import print_color


def get_info(count_type):
    # result is a list which contain all article infomation dics
    url = 'https://api.bilibili.com/x/article/rank/list?cid=%s&jsonp=jsonp' % (count_type)
    r = requests.get(url)
    if r.status_code == 200:
        string = r.text
        dic = json.loads(string)
        result = dic['data']
        return result
    else:
        print('cant connect')
        exit()


class Article(object):
    """docstring for Article"""

    def __init__(self, info_dic):
        super(Article, self).__init__()
        self.info_dic = info_dic
        for k, v in self.info_dic.items():
            setattr(self, k, v)
        self.exact_info()
        self.generate_result()

    def __repr__(self):
        return self.title

    def exact_info(self):
        self.url = 'https://www.bilibili.com/read/cv' + str(self.id)
        self.view = self.stats['view']
        self.reply = self.stats['reply']
        self.fav = self.stats['favorite']
        self.stat_string = 'score:{self.score}\tview:{self.view}\treply:{self.reply}\tfav:{self.fav}'.format(self=self)

    def generate_result(self):
        result_contents = [
            # '=' * 20,
            # 'title:' + self.title,
            self.url,
            'summary:' + self.summary,
            self.stat_string,
            '=' * 20
        ]
        self.result = '\n'.join(result_contents)

    def print_info(self):
        print_color('title:' + self.title, fore='red')
        print(self.result)


def run():
    count_type = input('1.month\t2.week\t3.day\t4.three_day')
    info_lst = get_info(count_type)
    articles = [Article(i) for i in info_lst]
    sorted(articles, key=lambda x: x.score)
    articles = list(reversed(articles))
    for i in articles:
        i.print_info()


'''
rank = {
    'day': '3',
    'three_day': '4',
    'week': '2',
    'month': '1'
}
'''
if __name__ == '__main__':
    while 1:
        run()
