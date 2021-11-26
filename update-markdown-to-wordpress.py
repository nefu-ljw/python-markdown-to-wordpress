# -*- coding: utf-8 -*-
# @Time : 2021/11/20 9:42
# @Author : nefu-ljw
# @File : update-markdown-to-wordpress.py
# @Function: Update an existing post in WordPress with a local Markdown file
# @Software: PyCharm
# @Reference: original


import os
import sys
import frontmatter
import markdown
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts, EditPost


def find_post(filepath, client):
    """
    find the post in WordPress by using filename in filepath as the searching title
    :param filepath: 更新用的文件路径
    :param client: 客户端
    :return True: if success
    """
    filename = os.path.basename(filepath)  # 例如：test(2021.11.19).md
    filename_suffix = filename.split('.')[-1]  # 例如：md
    filename_prefix = filename.replace('.' + filename_suffix, '')  # 例如：test(2021.11.19)；注意：这种替换方法要求文件名中只有一个".md"
    # 目前只支持 .md 后缀的文件
    if filename_suffix != 'md':
        print('ERROR: not Markdown file')
        return None
    # get pages in batches of 20
    offset = 0  # 每个batch的初始下标位置
    batch = 20  # 每次得到batch个post，存入posts中
    while True:  # 会得到所有文章，包括private(私密)、draft(草稿)状态的
        posts = client.call(GetPosts({'number': batch, 'offset': offset}))
        if len(posts) == 0:
            return None  # no more posts returned
        for post in posts:
            title = post.title
            if title == filename_prefix:
                return post
        offset = offset + batch


def update_post_content(post, filepath, client):
    """
    update a post in WordPress with the content in file path
    :param post: 已发布的文章（WordPressPost类型），由find_post函数得到
    :param filepath: 更新用的文件路径
    :param client: 客户端
    :return True: if success
    """
    post_from_file = frontmatter.load(filepath)  # 读取文档里的信息
    post_content_html = markdown.markdown(post_from_file.content,
                                          extensions=['markdown.extensions.fenced_code']).encode("utf-8")  # 转换为html
    post.content = post_content_html  # 修改内容
    return client.call(EditPost(post.id, post))


if __name__ == '__main__':
    # User Configuration
    filepath = 'your Markdown file path'  # e.g. D:/PythonCode/post-wordpress-with-markdown/doc/test.md
    domain = 'https://xxx.com'  # e.g. https://jwblog.xyz（配置了SSL证书就用https，否则用http）
    username = 'your username'
    password = 'your password'

    # Start Work
    if not os.path.isfile(filepath):
        print('FAILURE: not file path')
        sys.exit(1)

    client = Client(domain + '/xmlrpc.php', username, password)  # 客户端
    
    post = find_post(filepath, client)
    if post is not None:
        ret = update_post_content(post, filepath, client)
        if ret:
            print('SUCCESS to update the file: "%s"' % filepath)
        else:
            print('FAILURE to update the file: "%s"' % filepath)
    else:
        print('FAILURE to find the post. Please check your User Configuration and the title in your WordPress.')
