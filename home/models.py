from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
#from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.panels import FieldPanel
from wagtailvideos.edit_handlers import VideoChooserPanel
from blog.models import BlogPage


class HomePage(Page):

    Section1_Header = RichTextField(blank=True)
    Section1_Content = RichTextField(blank=True)
    Section2_Header = RichTextField(blank=True)
    gdc_bio_right_header = RichTextField(blank=True)
    gdc_bio_right_text = RichTextField(blank=True)
    Section4_Header = RichTextField(blank=True)
    Section4_Content = RichTextField(blank=True)
    Section5_Header = RichTextField(blank=True)
    Section5_Content = RichTextField(blank=True)
    Section6_Header = RichTextField(blank=True)
    Section6_Content = RichTextField(blank=True)

    instruments_bio = RichTextField(blank=True)
    aether_bio = RichTextField(blank=True)
    cape_bio = RichTextField(blank=True)
    mosaic_bio = RichTextField(blank=True)
    nemisis_bio = RichTextField(blank=True)
    tps_bio = RichTextField(blank=True)
    rem_bio = RichTextField(blank=True)
    instruments_lower_bio = RichTextField(blank=True)

    timeline_bio = RichTextField(blank=True)
    timeline_1_date = RichTextField(blank=True)
    timeline_1_header = RichTextField(blank=True)
    timeline_1_bio = RichTextField(blank=True)
    timeline_2_date = RichTextField(blank=True)
    timeline_2_header = RichTextField(blank=True)
    timeline_2_bio = RichTextField(blank=True)
    timeline_3_date = RichTextField(blank=True)
    timeline_3_header = RichTextField(blank=True)
    timeline_3_bio = RichTextField(blank=True)
    timeline_4_date = RichTextField(blank=True)
    timeline_4_header = RichTextField(blank=True)
    timeline_4_bio = RichTextField(blank=True)    
    timeline_footer = RichTextField(blank=True)

    gdc_about_video = models.ForeignKey('wagtailvideos.Video',
                                        related_name='+',
                                        null=True,
                                        on_delete=models.SET_NULL)

    aether_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    cape_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mosaic_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    nemisis_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tps_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    rem_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    timeline_1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    timeline_2_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    timeline_3_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    timeline_4_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    promote_panels = [
        FieldPanel('aether_logo'),
        FieldPanel('cape_logo'),
        FieldPanel('mosaic_logo'),
        FieldPanel('nemisis_logo'),
        FieldPanel('tps_logo'),
        FieldPanel('rem_logo'),
        FieldPanel('timeline_1_image'),
        FieldPanel('timeline_2_image'),
        FieldPanel('timeline_3_image'),
        FieldPanel('timeline_4_image'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('Section1_Header'),
        FieldPanel('Section1_Content'),
        FieldPanel('Section2_Header'),
        FieldPanel('gdc_bio_right_header'),
        FieldPanel('gdc_bio_right_text'),
        FieldPanel('Section4_Header'),
        FieldPanel('Section4_Content'),
        FieldPanel('Section5_Header'),
        FieldPanel('Section5_Content'),
        FieldPanel('Section6_Header'),
        FieldPanel('Section6_Content'),
        FieldPanel('instruments_bio'),
        FieldPanel('aether_bio'),
        FieldPanel('cape_bio'),
        FieldPanel('mosaic_bio'),
        FieldPanel('nemisis_bio'),
        FieldPanel('tps_bio'),
        FieldPanel('rem_bio'),
        FieldPanel('instruments_lower_bio'),
        FieldPanel('timeline_bio'),
        FieldPanel('timeline_1_date'),
        FieldPanel('timeline_1_header'),
        FieldPanel('timeline_1_bio'),
        FieldPanel('timeline_2_date'),
        FieldPanel('timeline_2_header'),
        FieldPanel('timeline_2_bio'),
        FieldPanel('timeline_3_date'),
        FieldPanel('timeline_3_header'),
        FieldPanel('timeline_3_bio'),
        FieldPanel('timeline_4_date'),
        FieldPanel('timeline_4_header'),
        FieldPanel('timeline_4_bio'),
        FieldPanel('timeline_footer'),
        VideoChooserPanel('gdc_about_video')
    ]


    def get_context (self,request,*args,**kwargs):
        context = super().get_context(request,*args,**kwargs)
        news = BlogPage.objects.live().order_by('-first_published_at')[:3]
        context["news"] = news
        return context
