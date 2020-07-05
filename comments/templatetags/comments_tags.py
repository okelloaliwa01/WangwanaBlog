#!/usr/bin/env python
# encoding: utf-8




from django import template
from django.template.loader import render_to_string
from ..models import Comment
from blog.models import Article
from comments.forms import CommentForm

register = template.Library()


@register.simple_tag
def parse_commenttree(commentlist, comment):
    """Get a list of sub-comments for the current review
        usage: {% parse_commenttree article_comments comment as childcomments %}
    """
    datas = []

    def parse(c):
        childs = commentlist.filter(parent_comment=c, is_enable=True)
        for child in childs:
            datas.append(child)
            parse(child)

    parse(comment)
    return datas


@register.inclusion_tag('comments/tags/comment_item.html')
def show_comment_item(comment, ischild):
    """comment"""
    depth = 1 if ischild else 2
    return {
        'comment_item': comment,
        'depth': depth
    }
