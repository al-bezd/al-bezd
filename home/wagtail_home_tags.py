"""
  When editing the content use the brackets:
  [[ <iframe>..</iframe> ]]
  And after, use it in templates like this:
  {{ page.body|resolve_html|richtext }}
"""
from django import template
register = template.Library()

@register.inclusion_tag('home/breadcrumbs_tag.html', takes_context=True)
def breadcrumbs(context):
    return {'main_page': context['self']}