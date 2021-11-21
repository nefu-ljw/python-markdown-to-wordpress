## 下载到本地

```bash
git clone https://github.com/nefu-ljw/python-markdown-to-wordpress
```
**注意：下载到本地后需要修改源代码。**

## 安装依赖项

我的运行环境：Python 3.7.10

```bash
pip3 install python-frontmatter
pip3 install markdown
pip3 install python-wordpress-xmlrpc
```

## 批量上传Markdown到WordPress

用pycharm打开`upload-markdown-to-wordpress.py`，**在主函数中修改**以下四行：

```python
path = 'your directory path or file path which store your Markdown files'  # e.g. D:/PythonCode/post-wordpress-with-markdown/doc
domain = 'https://xxx.com'  # e.g. https://jwblog.xyz（配置了SSL证书就用https，否则用http）
username = 'your username'
password = 'your password'
```

- path：本地存放Markdown文件的目录路径或单个文件路径
- domain：你的域名，例如我的网站 https://jwblog.xyz（配置了SSL证书就用https，否则用http）
- username：你的WordPress账号
- password：你的WordPress账号

可选项：

```python
post_metadata = {
    'category': ['博客存档'],  # 文章分类
    'tag': ['博客存档'],  # 文章标签
    'status': 'publish'  # 可选publish发布、draft草稿、private隐私状态
}
```

注意，如果要上传的Markdown文件中含有YMAL Front Matter，则默认其优先级更高，会覆盖代码中的可选项。

你可以在Markdown文件的最开始处添加YMAL Front Matter：

```yaml
---
category: [博客存档]
tag: [博客存档]
status: publish
---
```

目前只支持category（文章分类）、tag（文章标签）、status（文章状态）。默认文章开启评论。

代码修改完毕后，最后运行`upload-markdown-to-wordpress.py`，批量上传。

## 通过本地Markdown文件更新WordPress

如果上传某个Markdown文件后，本地修改了其内容，这时使用`update-markdown-to-wordpress.py`即可更新内容。

用pycharm打开`update-markdown-to-wordpress.py`，**在主函数中修改**以下四行：

```python
filepath = 'your directory path or file path which store your Markdown files'  # e.g. D:/PythonCode/post-wordpress-with-markdown/doc
domain = 'https://xxx.com'  # e.g. https://jwblog.xyz（配置了SSL证书就用https，否则用http）
username = 'your username'
password = 'your password'
```

目前只支持更新已上传WordPress的单个文章的内容。

**注意：本地Markdown文件名和WordPress文章的标题需要保持一致。**

代码修改完毕后，最后运行`update-markdown-to-wordpress.py`，更新内容。
