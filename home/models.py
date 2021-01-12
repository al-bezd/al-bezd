from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel
from django import forms


class HomePage(Page):
    pass

class PortfolioPage(Page):
    pass




















@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = verbose_name
    """Social media settings for our custom website."""

    vk = models.URLField(blank=True, null=True, help_text="VK URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    #youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")

    color_begin = ColorField(verbose_name='Цвет до наведения')
    color_after = ColorField(verbose_name='Цвет после наведения')
    transition  = models.FloatField(default=1, verbose_name='Время перетекания')

    panels = [
        MultiFieldPanel([
            FieldPanel("vk"),
            FieldPanel("instagram"),
   
            NativeColorPanel('color_begin'),
            NativeColorPanel('color_after'),
            FieldPanel("transition"),
        ], heading= 'Социальные сети')
    ]

@register_setting
class ContactSettings(BaseSetting):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name

    tel1     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №1", verbose_name="Телефон №1")
    tel2     = models.CharField(max_length=12, blank=True, null=True, help_text="Телефон №2", verbose_name="Телефон №2")
    email    = models.EmailField(blank=True, null=True, verbose_name="Email")

    panels = [
        MultiFieldPanel([
            FieldPanel("tel1"),
            FieldPanel("tel2"),
            FieldPanel("email"),

        ], heading="Контакты")
    ]
