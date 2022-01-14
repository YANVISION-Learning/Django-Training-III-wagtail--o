from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from website_blocks.blocks import hero, separators, features


class AboutPage(Page):

    body = StreamField([

        ('Hero1', hero.Hero1()),
        # Feature 2 added
        ('Features2', features.Feature2()),

    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ContactPage(Page):
    pass