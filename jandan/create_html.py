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


'''
def generate_html():
    pics = sort_pic()
    pics_strings = [generate_pic_html(i) for i in pics]
    pic_html_join = ''.join(pics_strings)
    with open('./format.html', 'r') as f:
        format_html = f.read()
    result = re.sub(r'\<insert\>', pic_html_join, format_html)
    with open('./1.html', 'w') as f:
        f.write(result)
'''


def divide_lst(pics, n):
    pics = sort_pic()
    total_pic = len(pics)
    # pages = total_pic // n
    result_lst = [pics[m: m + n] for m in range(total_pic) if m % n == 0]
    return result_lst


def generate_a_page_html(index, pages_count, pics_in_the_page):
    filename = './page' + str(index + 1) + '.html'
    pics_strings = [generate_pic_html(i) for i in pics_in_the_page]
    pic_html_join = ''.join(pics_strings)
    # page_html_format = '<a href="">previous</a>'
    page_part_htmls = ['<a href="./page%s.html">' % (i) + str(i) + ' </a>' for i in range(1, pages_count + 1)]
    page_bar = ''.join(page_part_htmls)
    with open('./format.html', 'r') as f:
        format_html = f.read()
    result = re.sub(r'\<insert\>', pic_html_join, format_html)
    result = re.sub(r'\<page\>', page_bar, result)
    with open(filename, 'w') as f:
        f.write(result)


def run():
    pics = sort_pic()
    pic_divide_lst = divide_lst(pics, 40)
    pages_count = len(pic_divide_lst)
    for index, content in enumerate(pic_divide_lst):
        generate_a_page_html(index, pages_count, content)
