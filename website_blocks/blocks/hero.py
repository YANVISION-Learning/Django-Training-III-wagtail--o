from django.db import models
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from website_blocks.blocks.links import Link


# StructBlock
#     # Block 1
#     # Block 2
class Hero1(blocks.StructBlock):
    title1 = blocks.CharBlock(default="Title 1", required=False)
    title2 = blocks.CharBlock(default="Title 2", required=False)
    title3 = blocks.CharBlock(default="Title 3", required=False)
    button = Link(help_text="Enter a link or select a page", required=False)
    background_image = ImageChooserBlock(help_text="Dimensions minimum: 1920x1280px")

    class Meta:
        template = 'website_blocks/hero/hero1.html'
        icon = 'image'
