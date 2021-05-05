from django.db import models

# Create your models here.
class blog(models.Model):
    author_name=models.CharField(max_length=50)
    author_artC=models.CharField(max_length=50)
    published_date=models.DateField()
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']
    