try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock
    wagtail_version = 1
except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock
    wagtail_version = 2
from wagtail.contrib.table_block.blocks import TableBlock

class SocialBlock(blocks.StructBlock):
    view = blocks.BooleanBlock(required=True, default=True)

    class Meta:
        template = 'home/social_block.html'
        # icon = "list-ul"

class Table(blocks.StreamBlock):
    table = TableBlock()