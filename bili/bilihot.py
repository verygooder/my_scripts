# coding=utf-8
import requests
import json
from pycolor import print_color


class Movie(object):
    """docstring for Movie"""

    def __init__(self, dic):
        super(Movie, self).__init__()
        self.dic = dic
        for k, v in self.dic.items():
            setattr(self, k, v)

    def __repr__(self):
        return self.title


def get_json(url):
    r = requests.get(url)
    string = r.text
    js = json.loads(string)
    return js


def get_lst(js):
    lst = js['hot']['list']
    movie_lst = []
    for i in lst:
        dic = i
        movie = Movie(dic)
        movie_lst.append(movie)
    return movie_lst


def print_info(movie):
    title = movie.title
    descr = movie.description
    play_time = movie.play
    barrage = movie.video_review
    duration = movie.duration
    aid = 'http://www.bilibili.com/video/av' + movie.aid
    """
    string = '片名:{title}\n内容:{descr}\n播放数:{play_time}\n弹幕数:{barrage}\n时长:{duration}\n链接:{aid}'.format(title=title, descr=descr, play_time=play_time, barrage=barrage, duration=duration, aid=aid)
    print(string)
    print('=' * 60)
    """
    string = '内容:{descr}\n播放数:{play_time}\n弹幕数:{barrage}\n时长:{duration}\n链接:{aid}'.format(descr=descr, play_time=play_time, barrage=barrage, duration=duration, aid=aid)
    print_color(title, fore='red')
    print(string)
    print('=' * 60)


foreign_url = 'https://www.bilibili.com/index/catalogy/145-week.json'
jap_url = 'https://www.bilibili.com/index/catalogy/146-week.json'
chi_url = 'https://www.bilibili.com/index/catalogy/147-week.json'
other_url = 'https://www.bilibili.com/index/catalogy/83-week.json'
name_lst = [
    '欧美',
    '日本',
    '国内',
    '其他'
]
url_lst = [
    foreign_url,
    jap_url,
    chi_url,
    other_url
]
choose_lst = list(zip(name_lst, url_lst))
while True:
    for x, y in enumerate(choose_lst):
        print(str(x + 1), y[0])
    print('choose anyone')
    command = int(input()) - 1
    choose = choose_lst[command]
    url = choose[1]
    js = get_json(url)
    lst = get_lst(js)
    for i in lst:
        print_info(i)
