from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    # Timeline Section
    timeline_1_bio = RichTextField()
    timeline_2_bio = RichTextField()
    timeline_3_bio = RichTextField()
    timeline_4_bio = RichTextField()
    timeline_1_header = RichTextField()
    timeline_2_header = RichTextField()
    timeline_3_header = RichTextField()
    timeline_4_header = RichTextField()
    timeline_1_date = RichTextField()
    timeline_2_date = RichTextField()
    timeline_3_date = RichTextField()
    timeline_4_date = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('timeline_1_bio'),
        FieldPanel('timeline_2_bio'),
        FieldPanel('timeline_3_bio'),
        FieldPanel('timeline_4_bio'),
        FieldPanel('timeline_1_header'),
        FieldPanel('timeline_2_header'),
        FieldPanel('timeline_3_header'),
        FieldPanel('timeline_4_header'),
        FieldPanel('timeline_1_date'),
        FieldPanel('timeline_2_date'),
        FieldPanel('timeline_3_date'),
        FieldPanel('timeline_4_date')
    ]