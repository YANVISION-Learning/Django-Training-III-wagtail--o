from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail_color_panel.blocks import NativeColorBlock


class SeparatorTextDescription(blocks.StructBlock):
    title = blocks.CharBlock(default="Title 1", required=False)
    description = blocks.RichTextBlock(default="RichText", required=False)
    background_color = NativeColorBlock(required=True)

    class Meta:
        template = 'website_blocks/separators/separator_text_description.html'
        icon = 'image'
