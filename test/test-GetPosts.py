# -*- coding: utf-8 -*-
# @Time : 2021/11/19 16:00
# @Author : nefu-ljw
# @File : test-GetPosts.py
# @Software: PyCharm
# @Reference: https://python-wordpress-xmlrpc.readthedocs.io/en/latest/examples/posts.html#advanced-querying

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts

client = Client('https://jwblog.xyz/xmlrpc.php', '账号', '密码')

# get pages in batches of 20
offset = 0  # 每个batch的初始下标位置
batch = 20  # 每次得到batch个post，存入posts中
# 会得到所有文章，包括private(私密)、draft(草稿)状态的
all_cnt = 0
while True:
    posts = client.call(GetPosts({'number': batch, 'offset': offset}))
    all_cnt = all_cnt + len(posts)
    if len(posts) == 0:
        break  # no more posts returned
    for post in posts:
        #title = post.title
        print(post)
    offset = offset + batch
print('-----------------------------------------------END-----------------------------------------------')
print('There are %d articles in your WordPress.' % all_cnt)
