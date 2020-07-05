#!/usr/bin/env python
# encoding: utf-8


from DjangoBlog.utils import send_email
from DjangoBlog.utils import get_current_site
import logging

logger = logging.getLogger(__name__)


def send_comment_email(comment):
    site = get_current_site().domain
    subject = 'Thanks for your comment'
    article_url = "https://{site}{path}".format(
        site=site, path=comment.article.get_absolute_url())
    html_content = """
                   <p>Thank you very much for your comments on this site</p>
                   You can visit
                   <a href="%s" rel="bookmark">%s</a>
                   To view your comments，
                   Thank you again！
                   <br />
                   If the link above cannot be opened，Please copy this link to your browser.
                   %s
                   """ % (article_url, comment.article.title, article_url)
    tomail = comment.author.email
    send_email([tomail], subject, html_content)
    try:
        if comment.parent_comment:
            html_content = """
                    You are in <a href="%s" rel="bookmark">%s</a> the comment of <br/> %s <br/> Received a reply, Go check it out
                    <br/>
                    If the link above cannot be opened，Please copy this link to your browser.
                    %s
                    """ % (article_url, comment.article.title, comment.parent_comment.body, article_url)
            tomail = comment.parent_comment.author.email
            send_email([tomail], subject, html_content)
    except Exception as e:
        logger.error(e)
