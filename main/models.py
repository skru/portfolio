from django.db import models
from tinymce.models import HTMLField

class Section(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=1024, blank=True)
    date = models.DateField()
    content = HTMLField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return self.title

class SectionImage(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="section_image"
    )
    image = models.ImageField(upload_to="images", blank=True)
    description = models.CharField(max_length=256, blank=True)

class SectionLink(models.Model):
	section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="section_link"
    )
	title = models.CharField(max_length=256)
	url = models.CharField(max_length=256)