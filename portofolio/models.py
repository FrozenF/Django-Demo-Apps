from django.db import models

# Create your models here.
class PortofolioItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/portfolio/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title