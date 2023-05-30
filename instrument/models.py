from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class InstrumentPage(Page):
    instrument_name = RichTextField(blank=True)
    about = RichTextField(blank=True)
    team = RichTextField(blank=True)
    Section_1 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('instrument_name'),
        FieldPanel('about'),
        FieldPanel('team'),
        FieldPanel('Section_1')
    ]