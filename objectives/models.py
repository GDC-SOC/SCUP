from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class ObjectivesPage(Page):
    about = RichTextField(default='<strong>Default header for about</strong><br>Default value for about')
    team = RichTextField(default='<strong>Default header for about</strong><br>Default value for about')
    Section_1 = RichTextField(default='Default value for Section_1')

    content_panels = Page.content_panels + [
        FieldPanel('about', heading='About Header'),
        FieldPanel('team', heading='Team Header'),
        FieldPanel('Section_1', heading='Section 1 Header')
    ]
