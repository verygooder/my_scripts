from googletrans import Translator
from sys import argv


def trans(string):
    trans = Translator(service_urls=['translate.google.cn'])
    ori = string
    result = trans.translate(ori, dest='en').text
    return (ori, result)


if __name__ == '__main__':
    string = argv[1]
    result = trans(string)[1]
    print(result)