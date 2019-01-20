"""
@Project   : movies
@Module    : fresh_apples.py
@Author    : Jeff [arfu.guo@gmail.com]
@Created   : 2019/1/20 下午10:42
@Desc      : 
"""
import webbrowser
import os


main_page_head = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--Viewport defines the area of screen that browser can render content to.
    width=device-width instructs the page to match the screen's width in device
    independent pixels by reflowing content. initial-scale=1.0 means a 1:1
    relationship between the device independent pixels and css pixels. Without
    initial-scale=1, some browers will keep the page width constant when rotating
    to landscape mode.-->

    <title>福云文集</title>
    <link rel="stylesheet"
     href="https://fonts.googleapis.com/css?family=Roboto:300,400,500">
    <link rel="stylesheet" href="main.css">
  </head>

  <body>

    <header class="container">
      <img class="header_logo" src="images/apple.gif" alt="udacity logo">
      <!--The default display of img is inline-block-->
      <section class="header_title">
        <h1 class="header_name">
          Jeff Guo
        </h1>
        <h3 class="header_career">
          Web Developer
        </h3>
      </section>
    </header>

    <main>

      <section class="color_and_picture">
        <section class="table">
          <section class="squ_words">
            <div class="square square1"></div>
            <h4 class="words">#02b3e4</h4>
          </section>
          <section class="squ_words">
            <div class="square square2"></div>
            <h4 class="words">#2d3c49</h4>
          </section>
          <section class="squ_words">
            <div class="square square3"></div>
            <h4 class="words">#7d97ad</h4>
          </section>
        </section>
        <img class="web_dev" src="images/web.png" alt="picture of web development">
      </section>
'''

main_page_section_before_r = '''
      <section class="work">
        <h2 class="work_title">推荐的文章</h2>
        <ul class="work_container">
'''

main_page_section_before_a = '''
        <h2 class="work_title">所有的文章</h2>
        <ul class="work_container">
'''

main_page_section_after_r = '''
        </ul>
'''

main_page_section_after_a = '''
        </ul>
      </section>

    </main>
  </body>
</html>        
'''

main_page_item = '''
<li class="github_work">
<h3 class="big_cap">
  <a href={article_url}>
  {article_title}
  </a>
</h3>
</li>
'''


def create_article_titles_content(articles):
    content = ''
    for article in articles:

        # Append the tile for the movie with its content filled in
        content += main_page_item.format(
            article_url=article.url,
            article_title=article.title + article.date
        )
    return content


def open_articles_page(articles_recommend, articles_all):
    # Create or overwrite the output file
    output_file = open('fresh_apples.html', 'w')

    rendered_content_r = create_article_titles_content(articles_recommend)
    rendered_content_a = create_article_titles_content(articles_all)

    # Output the file
    output_file.write(
        main_page_head + main_page_section_before_r + rendered_content_r +
        main_page_section_after_r + main_page_section_before_a +
        rendered_content_a + main_page_section_after_a)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
