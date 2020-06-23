from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portfolio/images")
    description = models.TextField()
    url = models.URLField(blank=True)