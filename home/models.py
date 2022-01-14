from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from website_blocks.blocks import hero, separators, features


class HomePage(Page):
    home_title = models.CharField(max_length=128, default="")
    home_body = RichTextField(blank=True)

    body = StreamField([

        ('Hero1', hero.Hero1()),
        ('SeparatorTextDescription', separators.SeparatorTextDescription()),
        ('Features1', features.Feature1()),
        ('RichText', blocks.RichTextBlock(default="RichText", required=False)),

    ])

    content_panels = Page.content_panels + [
        FieldPanel('home_title', classname="full"),
        FieldPanel('home_body', classname="full"),

        StreamFieldPanel('body'),
    ]
