from django import template
from home.models import SocialMediaSettings
from wagtail.core.models import Page
register = template.Library()


@register.inclusion_tag('home/social.html')
def social():
    return {'social': SocialMediaSettings.objects.all()[0]}


@register.inclusion_tag('home/social_as_ul.html')
def social_as_ul():
    return {'social': SocialMediaSettings.objects.all()[0]}


@register.inclusion_tag('home/social_as_ul.html')
def social_as_ul():
    return {'social': SocialMediaSettings.objects.all()[0]}


@register.inclusion_tag('home/site_map.html', takes_context=True)
def site_map(context):
    site_map = []
    for i in context['request'].site.root_page.get_children():
        if i.live:
            site_map.append(i)


    return {
        'site_map': site_map,
        'request': context['request'],
    }
