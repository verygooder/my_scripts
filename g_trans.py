from googletrans import Translator
from sys import argv


def trans(string):
    trans = Translator(service_urls=['translate.google.cn'])
    ori = string
    result = trans.translate(ori, dest='zh-CN').text
    return (ori, result)


string = argv[1]
trans_result = trans(string)[1]
print(trans_result)
