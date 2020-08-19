from django.db import models

class Info(models.Model):
	name = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	email = models.EmailField()
	github = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)

class Section(models.Model):
	title = models.CharField(max_length=256)
	sub_title = models.CharField(max_length=1024, blank=True)
	date = models.DateField()
	content = models.TextField()
	slug = models.SlugField(unique=True)
	external_link = models.URLField(blank=True)
	github_link = models.URLField(blank=True)
	image = models.ImageField(upload_to="images", blank=True)