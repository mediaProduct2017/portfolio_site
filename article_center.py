"""
@Project   : movies
@Module    : article_center.py
@Author    : Jeff [arfu.guo@gmail.com]
@Created   : 2019/1/20 下午11:09
@Desc      : 
"""
from article import Article
from fresh_apples import open_articles_page

articles_r = list()
articles_a = list()


def create_article_r(title, url, date="2019-01"):
    article = Article(title, url, date)
    articles_r.append(article)


def create_article_a(title, url, date="2019-01"):
    article = Article(title, url, date)
    articles_a.append(article)


if __name__ == "__main__":
    create_article_r('书到用时方恨烧', '201901/book_reading.pdf', '2018-10')
    create_article_a('道，德仁义礼', '201901/f1050.pdf', '2018-10')
    open_articles_page(articles_r, articles_a)
