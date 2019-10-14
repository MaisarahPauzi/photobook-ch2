from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_created')
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    slug = models.SlugField(max_length=100) # not unique
    caption = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.title} created by {self.user}'

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.user.username, self.pk, self.slug])
    
