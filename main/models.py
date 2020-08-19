from django.db import models
from tinymce.models import HTMLField

class Section(models.Model):
	title = models.CharField(max_length=256)
	sub_title = models.CharField(max_length=1024, blank=True)
	date = models.DateField()
	content = HTMLField()
	slug = models.SlugField(unique=True)
	external_link = models.URLField(blank=True)
	github_link = models.URLField(blank=True)
	image = models.ImageField(upload_to="images", blank=True)