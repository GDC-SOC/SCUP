from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.search import index

from rest_framework.fields import Field
from wagtail.api import APIField

# Create your models here.

class BlogChildPagesSerializer(Field):
    def to_representation(self, child_pages):
        return_posts = []
        for child in child_pages:
            post_dict={
                'id': child.id,
                'title': child.title,
                "slug": child.slug,
                "url": child.url
            }
            return_posts.append(post_dict)
        return return_posts
    
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    api_fields = [
        APIField("posts", serializer=BlogChildPagesSerializer(source='get_child_pages')),
    ]

    @property
    def get_child_pages(self):
        return self.get_children().live()

    def get_context (self,request,*args,**kwargs):
        context = super().get_context(request,*args,**kwargs)
        all_posts = BlogPage.objects.live().order_by('-first_published_at')
        # Number in this paginator determines posts per page
        paginator = Paginator(all_posts, 5)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
       
        except PageNotAnInteger:
            posts = paginator.page(1)
        
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context ["posts"] = posts
        return context

class BlogPage(Page):
    date = models.DateField("Post date")
    summary = RichTextField(
        max_length=500, 
        null=True,
        features=['bold', 
                  'italic', 
                  'underline', 
                  'link', 
                  'fontsize',
                  'h2', 
                  'h3', 
                  'superscript', 
                  'subscript', 
                  'ul', 
                  'ol', 
                  'hr', 
                  'strikethrough',
                  ], 
        )
        
    body = RichTextField(blank=True)
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    )

    stream_body = StreamField([
        ('paragraph', blocks.RichTextBlock(null=True)),
        ('captioned_image', blocks.StructBlock([
            ('picture', ImageChooserBlock(required=False)),
            ('caption', blocks.RichTextBlock(max_length=255))
        ]))
    ])
    

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]


    promote_panels = Page.promote_panels + [ 
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('blog_image'),
        FieldPanel('summary'),
        FieldPanel('body'),
        FieldPanel('stream_body')

    ]
