from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(null=True, blank=True, upload_to="projects/%Y/%m/%d/", default="default.jpg")
    project_description = models.CharField(max_length=200)
    description_full = models.TextField(null=True, blank=True)
    what_we_did = models.CharField(max_length=200)
    what_we_did_full = models.TextField(null=True, blank=True)
    lightbox_image = models.ImageField(null=True, blank=True, upload_to="projects/%Y/%m/%d/", default="default.jpg")
    client = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    data_start = models.DateField()
    data_end = models.DateField()
    project_value = models.IntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=200)


def __str__(self):
    return self.title
