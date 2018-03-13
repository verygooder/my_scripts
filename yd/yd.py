import requests
from bs4 import BeautifulSoup
from sys import argv


header = {
    'Host': 'dict.youdao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; webDict_HdAD=%7B%22req%22%3A%22http%3A//dict.youdao.com%22%2C%22width%22%3A960%2C%22height%22%3A240%2C%22showtime%22%3A5000%2C%22fadetime%22%3A500%2C%22notShowInterval%22%3A3%2C%22notShowInDays%22%3Afalse%2C%22lastShowDate%22%3A%22Mon%20Nov%2008%202010%22%7D; ___rl__test__cookies=1520943679583; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; ___rl__test__cookies=1520944029401; YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=2024948036@59.111.179.154; JSESSIONID=abcJp28qLNw4O5elLtFiw; ___rl__test__cookies=1520943651997; OUTFOX_SEARCH_USER_ID_NCOO=1538471218.2110572; search-popup-show=3-13',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


def getDefine(word):
    url_root = 'http://dict.youdao.com/w/'
    url = url_root + word
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return exeContent(r)
    else:
        return 'Connection fail'


def exeContent(r):
    soup = BeautifulSoup(r.text, 'html5lib')
    div = soup.find('div', id='phrsListTab')
    if div:
        text = div.getText()
        result = ''.join(text.split())
        return result
    else:
        return 'No Define'


if __name__ == '__main__':
    word = argv[1]
    print(getDefine(word))