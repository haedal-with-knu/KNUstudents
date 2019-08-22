from django.db import models

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='instructions/his/', default='null')
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.postname
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

class Photo(models.Model):
    image = models.ImageField(upload_to='instructions/img/')
