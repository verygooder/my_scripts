# coding=utf-8
import re


class Pic(object):
    """docstring for Pic"""

    def __init__(self, data_tuple):
        super(Pic, self).__init__()
        self.data = data_tuple
        self.rate = self.data[0]
        self.url = self.data[1]
        self.id = self.data[2]

    def __repr__(self):
        return ', '.join([str(self.rate), self.id])


def sort_pic():
    with open('./result.tsv', 'r') as f:
        data = f.readlines()
    data = [i.strip() for i in data]
    data_tuple_lst = [tuple(i.split('\t')) for i in data]
    pics = [Pic(i) for i in data_tuple_lst]
    pics = sorted(pics, key=lambda x: float(x.rate), reverse=True)
    return pics


def generate_pic_html(pic_obj):
    '''
    format:
    <a target="_blank" href="http://wx2.sinaimg.cn/large/661eb95cgy1ficn7hr55dj21e01e0alk.jpg">
        <img src="http://wx2.sinaimg.cn/large/661eb95cgy1ficn7hr55dj21e01e0alk.jpg", height="160">
       "3.14"
    </a>
    '''
    url = pic_obj.url
    # rate = pic_obj.rate
    # pic_id = pic_obj.id
    line1 = '<a target="_blank" href="%s">' % url
    line2 = '<img src="%s", height="160">' % url
    line3 = ' '
    line4 = '</a>'
    result = ''.join([line1, line2, line3, line4])
    return result


def generate_html():
    pics = sort_pic()
    pics_strings = [generate_pic_html(i) for i in pics]
    pic_html_join = ''.join(pics_strings)
    with open('./format.html', 'r') as f:
        format_html = f.read()
    result = re.sub(r'\<insert\>', pic_html_join, format_html)
    with open('./1.html', 'w') as f:
        f.write(result)
