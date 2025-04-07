#
# import re
#
# def replace_chunk(content, marker, chunk, inline=False):
#     r = re.compile(
#         r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
#             re.DOTALL,
#     )
#     if not inline:
#         chunk = '\n{}\n'.format(chunk)
#     chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
#     return r.sub(chunk, content)
