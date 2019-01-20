"""
@Project   : movies
@Module    : article.py
@Author    : Jeff [arfu.guo@gmail.com]
@Created   : 2019/1/20 下午11:07
@Desc      : 
"""


class Article:

    def __init__(self, title, url, date):
        self.title = title
        self.url = 'articles/' + url
        self.date = date
