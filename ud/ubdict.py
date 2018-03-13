import requests
from bs4 import BeautifulSoup
from sys import argv


header = {
	'Host': 'www.urbandictionary.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.urbandictionary.com/',
	'Cookie': '_sp_ses.5c9c=*; _sp_id.5c9c=fed36eb1-17e1-49e5-8bd0-88071b350bf2.1520945282.1.1520945289.1520945282.ec8998a1-3cbd-4755-96bb-5f9cabb209df; sixpack_client_id=be30e2d6-0062-41cd-9da3-33561ff96cc2',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'
}


def getDefine(word):
	url_root = 'https://www.urbandictionary.com/define.php?term='
	url = url_root + word
	r = requests.get(url, headers=header)
	if r.status_code == 200:
		result = exeSource(r)
		return result
	else:
		return 'Cant connect'


def exeSource(r):
	soup = BeautifulSoup(r.text, 'html5lib')
	divs = soup.find_all('div', class_='def-panel')
	if divs:
		define_strings = [exeDiv(div) for div in divs]
		return define_strings
	else:
		return ['No define']


def exeDiv(div):
	meaning = div.find('div', class_='meaning')
	example = div.find('div', class_='example')
	dic = {
		'meaning': 'none',
		'example': 'none'
	}
	if meaning:
		dic['meaning'] = meaning.getText()
	if example:
		dic['example'] = example.getText()
	string = 'meaning\n' + dic['meaning'] + '\n' + 'example:\n' + dic['example']
	return string


if __name__ == '__main__':
	word = argv[1]
	result_lst = getDefine(word)
	for index, value in enumerate(result_lst):
		string = str(index + 1) + ':' + value
		print(string)
		print('=' * 20)
