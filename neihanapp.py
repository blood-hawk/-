# -*-coding:utf8-*-
# "__author__" = "Black Hawk"
import urllib2
import re
import codecs


def save_file(data):
    path = 'H:\\joke.txt'
    f = codecs.open(path, 'a+','utf-8')
    f.write(data+'\r\n')


def load_page(page):
    url = "http://www.neihan8.com/article/index_" + str(page) + ".html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             'Chrome/61.0.3163.100 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(req)
    html = res.read()
    # return new_html
    pattern = re.compile(r'<div class="text-column-item box box-790">(.*?)</a></i></div>', re.S)
    item_list = pattern.findall(html)
    return item_list


if __name__ == '__main__':
    item_list = load_page(2)
    for item in item_list:
        data=item.replace('<p>', ' ').replace('</p>', ' ').replace('<br>', ' ')
        print "download......"
        save_file(data)