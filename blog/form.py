# -*- coding: utf-8 -*
# Author Seichung

from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    """
    文章编写表单类
    forms.ModelForm:适合于需要直接与数据库交互的功能，比如新建、更新数据库的字段等
    """
    # 格式需要是Meta，否则会报错
    class Meta:
        # 数据模型来源
        model = Article
        # 表单涉及的字段
        fields = ('title', 'content')
