from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'article'  # 该名字必须与app文件夹名称一致
    verbose_name = '文章'   # 汉化名字