from django.db import models

class Article(models.Model):
    title = models.CharField("Article's title", max_length=200)
    description = models.CharField("Short description of the Article (for SEO)", max_length=300)
    body = models.TextField("Article's body")
    image = models.ImageField(upload_to="articles_images")
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


class Services(models.Model):
    name = models.CharField("Service's name", max_length=(200))
    description = models.TextField("Service's Description")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Order(models.Model):
    name = models.CharField("Your name", max_length=100)
    phone = models.CharField("Your phone", max_length=100)
    company = models.CharField("Your company", max_length=100, blank=True)
    order_from = models.CharField("The Order will be shipped from", max_length=200)
    order_to = models.CharField("The Order will be shipped to", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer's Order"
        verbose_name_plural = "Customer's Orders"


class Fleet(models.Model):
    name = models.CharField("Fleet's name", max_length=(200))
    description = models.TextField("Fleet's Description")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fleet"
        verbose_name_plural = "Fleets"


class Project(models.Model):
    name = models.CharField("Project's name", max_length=(200))
    description = models.TextField("Project's Description")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"