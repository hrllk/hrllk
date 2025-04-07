#
# import feedparser
#
# def fetching_writing():
#     entries = feedparser.parse('https://hrllk.github.io/feed.xml')['entires'][:5]
#     return [
#         {
#             'title': entiry['title'],
#             'url': entry['link'].split('#')[0],
#             'published': re.findall(r'(.*?)\s00:00', entry['published'])[0]
#         }
#         for entry in entries
#     ]
