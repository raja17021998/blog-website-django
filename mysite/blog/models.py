from django.db import models
from django.utils import timezone
# from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author= models.ForeignKey('auth.User',on_delete=models.CASCADE,) # author connected to superuser on the website
    title= models.CharField(max_length=250)
    text= models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True) # analogous to approved comment


    def publish(self):
        self.published_date= timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post= models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE,)
    author= models.CharField(max_length=264)
    text= models.TextField()
    created_date= models.DateField(default=timezone.now())
    approved_comment= models.BooleanField(default=False)  # analogous to published date

    def approve(self):
        self.approved_comment= True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def _str__(self):
        return self.text