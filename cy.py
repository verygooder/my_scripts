import requests
import json
from sys import argv


class Translator(object):
    def __init__(self):
        self.url = "http://api.interpreter.caiyunai.com/v1/translator"
        self.token = "p1p507xjz96zqd4itudw"
        self.headers = {
            'content-type': "application/json",
            'x-authorization': "token " + self.token
        }

    def trans_sentences(self, source_sentences, lang_argv):
        payload = {
            "source": source_sentences,
            "trans_type": {"-c": "en2zh", "-e": "zh2en"}[lang_argv],
            "request_id": "demo"
        }
        r = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        if r.status_code == 200:
            result = json.loads(r.text)['target']
            return result
        else:
            return ['network error']

    def trans_paragraph(self, paragraph, lang_argv):
        sentences = paragraph.split('.')
        sentences = [i for i in sentences if i != '']
        sentences = [i + '.' for i in sentences]
        trans_result = self.trans_sentences(sentences, lang_argv)
        result = ''.join(trans_result)
        return result


def main():
    data = argv[2]
    tr = Translator()
    result = tr.trans_paragraph(data, argv[1])
    print(result)


if __name__ == '__main__':
    main()
