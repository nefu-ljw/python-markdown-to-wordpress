# -*- coding: utf-8 -*-
# @Time : 2021/11/18 20:50
# @Author : nefu-ljw
# @File : test-Newpost.py
# @Software: PyCharm
# @Reference: original

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

post = WordPressPost()  # 初始化post，我们要发表的文章就是post

# post的一些属性
post.title = "Test: This is the title"  # 标题
post.content = "Test: This is the content"  # 内容
post.post_status = 'publish'  # 类型（publish发布、draft草稿、private隐私）
post.terms_names = {
    'post_tag': ['test-tag1', 'test-tag2'],  # 标签(可以写多个)
    'category': ['test-category']  # 分类(可以写多个)
}  # 如果标签、分类没有的话会自动创建，有的话也不影响
post.comment_status = 'open'  # 开启评论

# 客户端
client = Client('https://jwblog.xyz/xmlrpc.php', '账号', '密码')  # 改成自己的账号密码，jwblog.xyz改成你自己的域名
client.call(NewPost(post))
