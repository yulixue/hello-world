from bs4 import BeautifulSoup
import requests
import re
from time import sleep
import sys

def get_html_text(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def get_comment(html, comment):
    soup = BeautifulSoup(html, 'lxml')
    comments = soup.find_all('span', class_='short')
    #for item in comments:
    #    print(item.string)
    for item in comments:
        comment.append(item.string)

def get_score(html, score):
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    star = re.findall(pattern, html)
    s = 0
    for item in star:
        s += int(item)
    score.append(s)

def main():
    comment = []
    score = []
    for i in range(1,4):
        url = 'https://book.douban.com/subject/1291204/comments/'
        url = url + 'hot?p=' + str(i)
        print(url)
        html = get_html_text(url)
        get_comment(html, comment)
        get_score(html, score)
        sleep(30)
    for k, v in zip(range(1,len(comment)+1),comment):
        try:
            print("{:>2}. {}".format(k,v))
        except UnicodeEncodeError:
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode+1), 0xfffd)
            print("{:>2}. {}".format(k, v.translate(non_bmp_map)))
    #print("共有{}人打分，总分：{}，平均分：{:.2}。".format(len(star), s, s/len(star)))
    print("总分：",sum(score))

main()
