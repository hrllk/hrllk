#
# import feedparser
# import time
#
# URL = "https://hrllk.github.io/feed.xml"
# RSS_FEED = feedparser.parse(URL)
# MAX_POST = 7
#
# markdown_text = """
#
# ## About Me
# Hello! My name is Hwiryung Kim, and I'm a dedicated backend developer with a passion for crafting clean, efficient code and solving complex problems. With a strong foundation in Java and expertise in the Spring framework, I thrive in architecting robust systems that stand the test of time. 
#
# In addition, I have a keen interest in design patterns and their application to solving real-world problems. Whether it's implementing creational, structural, or behavioral patterns, I leverage these patterns to improve code readability, flexibility, and maintainability.
#
# Above all, I consider myself a problem solver at heart. I thrive on tackling challenges head-on, breaking them down into manageable tasks, and finding innovative solutions to overcome them. I'm always eager to learn new technologies and methodologies to expand my skill set and stay ahead in this dynamic field.
#
# ##  Posts
# """
#
# for idx, feed in enumerate(RSS_FEED['entries']):
#     if idx > MAX_POST:
#         break
#     else:
#         feed_date = feed['published_parsed']
#         markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {
#             feed['title']}]({feed['link']}) <br/>\n"
#
# f = open("README.md", mode="w", encoding="utf-8")
# f.write(markdown_text)
# f.close()
