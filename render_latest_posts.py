
import feedparser
import time

URL = "https://hrllk.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

markdown_text = """
<!-- header -->
<!-- ![header](https://capsule-render.vercel.app/api?type=transparent&color=auto&height=300&section=header&text=:\)&fontSize=90) -->
<!-- Hi, 🙋🏻‍♂️ I'm backend developer <br> -->
<!-- I love listening lofi <br> -->
<!-- [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhrllk%2F&count_bg=%23D4E7F0&title_bg=%2378BBD8&icon=&icon_color=%23B8B8B8&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) -->

<!-- ## Hi There, I'm HwiRyung :) -->


## About Me
Hello! My name is Hwiryung Kim, and I'm a dedicated backend developer with a passion for crafting clean, efficient code and solving complex problems. With a strong foundation in Java and expertise in the Spring framework, I thrive in architecting robust systems that stand the test of time. 

In addition, I have a keen interest in design patterns and their application to solving real-world problems. Whether it's implementing creational, structural, or behavioral patterns, I leverage these patterns to improve code readability, flexibility, and maintainability.

Above all, I consider myself a problem solver at heart. I thrive on tackling challenges head-on, breaking them down into manageable tasks, and finding innovative solutions to overcome them. I'm always eager to learn new technologies and methodologies to expand my skill set and stay ahead in this dynamic field.

##  Posts
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {
            feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
