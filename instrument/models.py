from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class InstrumentPage(Page):
    instrument_name = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('instrument_name')
    ]