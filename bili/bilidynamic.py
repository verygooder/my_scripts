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
        'Cookie': 'l=v; LIVE_BUVID=c40ae155cb78121f2e07ec76605e0f1f; buvid3=A8F8CB4D-26D6-4A58-941E-13A233F3F52826540infoc; sid=63fc3x9r; fts=1510722266; LIVE_BUVID__ckMd5=00c4d10af2f0973a; rpdid=olwimixlkidosoiwlqoww; LIVE_PLAYER_TYPE=2; finger=dbd0cac5; DedeUserID=766568; DedeUserID__ckMd5=16c20f677710b2d7; SESSDATA=ce23596f%2C1515915147%2C9dfd6100; bili_jct=7cd98746cf284b40d5cfe82aec17f4e3; _dfcaptcha=0b5ed5479256d03bfe03222f671cb0fa; _cnt_pm=0; _cnt_notify=39',
        'Host': 'api.vc.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
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
