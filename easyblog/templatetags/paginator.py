import logging

from django import template
from django.core.paginator import Page

logger = logging.getLogger(__name__)

class PaginatorNode(template.Node):
    def __init__(self, current_page, total_pages):
        self.current_page = template.Variable(current_page)
        self.total_pages = template.Variable(total_pages)
        
    def render(self, context):       
        current_page = self.current_page.resolve(context)
        total_pages = self.total_pages.resolve(context)
        previous_page = current_page - 1
        next_page = current_page + 1
         
        html = '<ul>\n'
        if current_page > 1:
            html += '<li class="prev"><a href="?page=%u">&larr; Previous</a></li>' % previous_page
        else:
            html += '<li class="prev disabled"><a href="#">&larr; Previous</a></li>'
        
        html += "\n"
        
        for page_num in range(1, total_pages + 1):
            html += '<li'
            if (current_page == page_num):
                html += ' class="active"'
            html += '><a href="?page=%u">%u</a></li>' % (page_num, page_num)
            html += "\n"
            
        
        if current_page < total_pages:
            html += '<li class="next"><a href="?page=%u">Next &rarr;</a></li>' % next_page
        else:
            html += '<li class="next disabled"><a href="#">Next &rarr;</a></li>'
      
        return html

def do_paginator(parser, token):
    try:
        tag_name, current_page, total_pages = token.split_contents()                                      
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a two arguments" % token.contents.split()[0])      
    return PaginatorNode(current_page, total_pages)


register = template.Library()

register.tag('paginator', do_paginator)