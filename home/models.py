from django.db import models


from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from django import forms
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.models import Page, AbstractPage, Orderable
from wagtail.search import index
from home.blocks import SocialBlock, Table
from mysite.settings import dev
from wagtail_blocks.blocks import default_blocks, RowBlock, CKEditor5Block
from wagtail.images.edit_handlers import ImageChooserPanel
from django.template.defaultfilters import slugify as django_slugify
from django.utils.translation import gettext_lazy as _

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class HomePage(Page):
    #body = StreamField(default_blocks() + [
    #    ('Row', RowBlock()),
    #    ('Social', SocialBlock())
    #])
    skills = StreamField([
        ('Table',Table())
        ])

    content_panels = Page.content_panels + [
        #StreamFieldPanel("body"),
        StreamFieldPanel('skills'),
    ]

    PAGE_TEMPLATE_VAR = 'page'

    def get_context(self, request, *args, **kwargs):
        context = {
            self.PAGE_TEMPLATE_VAR: self,
            'self': self,
            'request': request,
        }

        if self.context_object_name:
            context[self.context_object_name] = self

        context['menuitems'] = Page.objects.filter(
            live=True,
            show_in_menus=True
        )
        context['portfolio'] = PortfolioPage.objects.all()[0:5]

        return context

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class PortfolioPage(Page):
    name = models.CharField(max_length=128)
    section_des = models.TextField(blank=True, null=True) #section-des
    body        = models.TextField(blank=True, null=True) #content-670

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel("section_des", classname="full"),
        FieldPanel("body", classname="full"),
        

    ]

    PAGE_TEMPLATE_VAR = 'page'

    def get_context(self, request, *args, **kwargs):
        context = {
            self.PAGE_TEMPLATE_VAR: self,
            'self': self,
            'request': request,
        }

        if self.context_object_name:
            context[self.context_object_name] = self

        context['menuitems'] = Page.objects.filter(
            live=True,
            show_in_menus=True
        )

        return context

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(PortfolioPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
  

    panels = [
        ImageChooserPanel('image'),
     
    ]


class SingleBlogPage(Page):

    body = StreamField(
        default_blocks() + [('Row', RowBlock()), ('Social', SocialBlock())], blank=True)
    content_panels = Page.content_panels + [StreamFieldPanel("body")]

    PAGE_TEMPLATE_VAR = 'page'

    def get_context(self, request, *args, **kwargs):
        context = {
            self.PAGE_TEMPLATE_VAR: self,
            'self': self,
            'request': request,
        }

        if self.context_object_name:
            context[self.context_object_name] = self

        context['menuitems'] = Page.objects.filter(
            live=True,
            show_in_menus=True
        )

        return context

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = verbose_name
    vk = models.URLField(blank=True, null=True, help_text="VK URL")
    instagram = models.URLField(
        blank=True, null=True, help_text="Instagram URL")
    panels = [
        MultiFieldPanel([
            FieldPanel("vk"),
            FieldPanel("instagram"),
        ], heading='Социальные сети')
    ]


@register_setting
class ContactSettings(BaseSetting):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name

    tel1 = models.CharField(max_length=12, blank=True, null=True,
                            help_text="Телефон №1", verbose_name="Телефон №1")
    tel2 = models.CharField(max_length=12, blank=True, null=True,
                            help_text="Телефон №2", verbose_name="Телефон №2")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    panels = [
        MultiFieldPanel([
            FieldPanel("tel1"),
            FieldPanel("tel2"),
            FieldPanel("email"),

        ], heading="Контакты")
    ]

@register_setting
class PhotoMainPageSettings(BaseSetting):
    class Meta:
        verbose_name = 'Фотографии главной страницы'
        verbose_name_plural = verbose_name

    main_photo = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')
    contact_photo = models.ForeignKey(
        'wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        ImageChooserPanel('main_photo'),
        ImageChooserPanel('contact_photo'),
    ]