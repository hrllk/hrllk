
import feedparser, time

URL="https://hrllk.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
<!-- header -->
![header](https://capsule-render.vercel.app/api?type=transparent&color=auto&height=300&section=header&text=:\)&fontSize=90)
Hi, 🙋🏻‍♂️ I'm backend developer using Java and Spring 
I love listening to lofi & minecraft music
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhrllk%2F&count_bg=%23D4E7F0&title_bg=%2378BBD8&icon=&icon_color=%23B8B8B8&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
## 📚 Stacks 
<div>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/>
  <img src="https://img.shields.io/badge/JQuery-0769AD?style=flat-square&logo=JQuery&logoColor=white"/>
</div>
<div>
  <img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white"/> 
  <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white"/>
</div>
<img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=RabbitMQ&logoColor=white"/>
<div>
  <img src="https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=MariaDB&logoColor=white"/> 
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 
</div>
<div>
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=Jenkins&logoColor=white"/> 
  <img src="https://img.shields.io/badge/AmazonEC2-FF9900?style=flat-square&logo=AmazonEC2&logoColor=white"/> 
  <img src="https://img.shields.io/badge/AmazonS3-569A31?style=flat-square&logo=AmazonS3&logoColor=white"/> 
  <img src="https://img.shields.io/badge/AmazonRDS-527FFF?style=flat-square&logo=AmazonRDS&logoColor=white"/> 
</div>
<div>
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/> 
  <img src="https://img.shields.io/badge/Confluence-172B4D?style=flat-square&logo=Confluence&logoColor=white"/> 
</div>
<div>
  <img src="https://img.shields.io/badge/JetBrains-000000?style=flat-square&logo=JetBrains&logoColor=white"/> 
  <img src="https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=Neovim&logoColor=white"/> 
</div>
 

## ⭐️ Stats
![Hrllk's GitHub stats](https://github-readme-stats.vercel.app/api?username=hrllk&show_icons=true&theme=merko)

## ⛏️ Recent Posts
"""

print('hi!!')
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break;
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
