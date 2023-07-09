from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
#from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.panels import FieldPanel

class InstrumentPage(Page):
    instrument_logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    )

    instrument_name = RichTextField(blank=True)
    PI_photo= models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    ) 
    PI = RichTextField(blank=True)
    DPI_photo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    ) 
    DPI = RichTextField(blank=True)
    instrument_scientist_photo = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    ) 
    instrument_scientist = RichTextField(blank=True)
    institutions = RichTextField(blank=True)
    instrument_summary = RichTextField(blank=True)
    measurements = RichTextField(blank=True)
    data_products = RichTextField(blank=True)
    realtime_products = RichTextField(blank=True)
    image_of_instrument = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    ) 
    instrument_parameters = RichTextField(blank=True)
    operation_principles = RichTextField(blank=True)
    operation_concept = RichTextField(blank=True)
    heritage = RichTextField(blank=True)
    team = RichTextField(blank=True)
    documents = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('instrument_logo'),
        FieldPanel('instrument_name'),
        FieldPanel('PI_photo'),
        FieldPanel('PI'),
        FieldPanel('DPI_photo'),
        FieldPanel('DPI'),
        FieldPanel('instrument_scientist_photo'),
        FieldPanel('instrument_scientist'),
        FieldPanel('institutions'),
        FieldPanel('instrument_summary'),
        FieldPanel('measurements'),
        FieldPanel('data_products'),
        FieldPanel('realtime_products'),
        FieldPanel('image_of_instrument'),
        FieldPanel('instrument_parameters'),
        FieldPanel('operation_principles'),
        FieldPanel('operation_concept'),
        FieldPanel('heritage'),
        FieldPanel('team'),
        FieldPanel('documents')
    ]