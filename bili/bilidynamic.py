# bili dynamic
# coding=utf-8
import requests
import json
from pycolor import print_color


def get_info():
    # return a list contained dynamics info
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Host': 'api.vc.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
    with open('./dyn_cookie', 'r') as f:
        cookie = f.read().strip()
    headers['Cookie'] = cookie
    url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=766568&type=268435455'
    r = requests.get(url, headers=headers)
    info = json.loads(r.text)
    result = info['data']['cards']
    return result


class Entry(object):
    """docstring for Entry"""

    def __init__(self, dic):
        super(Entry, self).__init__()
        self.dic = dic
        for k, v in self.dic.items():
            setattr(self, k, v)
        self.exact_info()
        self.generate_result()

    def exact_info(self):
        self.up = self.desc['user_profile']['info']['uname']
        self.card_info = json.loads(self.card)
        self.title = self.card_info.get('title', 'null')
        self.descr = self.card_info.get('desc', 'null')
        self.av = str(self.card_info.get('aid', 'null'))
        self.url = 'https://www.bilibili.com/video/av' + self.av

    def generate_result(self):
        result_contents = [
            # self.title,
            self.url,
            self.descr,
            self.up,
            '=' * 20
        ]
        self.result = '\n'.join(result_contents)


if __name__ == '__main__':
    info_lst = get_info()
    entrys = [Entry(i) for i in info_lst]
    entrys = [i for i in entrys if i.title != 'null']
    # sorted(entrys, reverse=True)
    entrys = list(reversed(entrys))
    for i in entrys:
        print_color(i.title, fore='red')
        print(i.result)
