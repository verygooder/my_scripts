import requests
import re
import json
from textrank4zh import TextRank4Sentence
from sys import argv


def diffbot_response(url):
    root = 'https://labs.diffbot.com/testdrive/article?'
    tail1 = 'callback=jQuery1111041624261867318824_1539839965048&token=testdriverehjenztgeil&url='
    tail2 = '&format=jsonp'
    url = root + tail1 + url + tail2
    print('diffbot executing...')
    r = requests.get(url)
    print('diffbot executed successfully')
    return r.text


def extract_diffbot_response(text):
    text = re.sub('jQuery.*?\(', '', text)
    text = text[:-1]
    dic = json.loads(text)
    result = dic['objects'][0]['text']
    # result = re.sub('\n', '', result)
    return result


def text_abstract(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text)
    sentences_count = len(tr4s.sentences) // 4
    if sentences_count <= 6:
        sentences_num = sentences_count
    else:
        sentences_num = 6
    abstract_sentences = tr4s.get_key_sentences(num=sentences_num)
    abstract_sentences.sort(key=lambda x: x['index'])
    return abstract_sentences


def run():
    url = argv[1]
    text = diffbot_response(url)
    text = extract_diffbot_response(text)
    sentences = text_abstract(text)
    print(text + '\n')
    print('*' * 20)
    for i in sentences:
        print(i['sentence'] + '\n')
    return 0


if __name__ == '__main__':
    run()
