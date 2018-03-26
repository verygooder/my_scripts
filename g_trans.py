from googletrans import Translator
from sys import argv


def trans(string, dest_language):
    trans = Translator(service_urls=['translate.google.cn'])
    ori = string
    result = trans.translate(ori, dest=dest_language).text
    return (ori, result)


dest_dic = {
    'c': 'zh-CN',
    'e': 'en'
}
dest_language = dest_dic[argv[1]]
string = argv[2]
trans_result = trans(string, dest_language)[1]
print(trans_result)
