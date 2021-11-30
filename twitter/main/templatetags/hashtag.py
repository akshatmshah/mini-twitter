from django import template
import re
from django.utils.safestring import mark_safe
from django.utils.html import escape


register = template.Library()

def generate_link(link):
    return '<a class="link" href="{}">{}</a>'.format(link, link)

def generate_hashtag_link(tag):
    url = "/feed/{}".format(tag)
    return '<a class="hashtag" href="{}">#{}</a>'.format(url, tag)


@register.filter
def render_content(obj):
    text = re.sub(r"#(\w+)", lambda m: generate_hashtag_link(m.group(1)),obj)
    return mark_safe(re.sub(r"(https?://[^\s]+)", 
        lambda m: generate_link(m.group(1)), text))