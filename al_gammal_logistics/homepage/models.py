from django.db import models

class Article(models.Model):
    title = models.CharField("Article's title", max_length=200)
    description = models.CharField("Short description of the Article (for SEO)", max_length=300)
    body = models.TextField("Article's body")
    image = models.ImageField(upload_to="Articles images")
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Jobs(models.Model):
    title = models.CharField("Job title", max_length=150)
    description = models.TextField("Job description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"