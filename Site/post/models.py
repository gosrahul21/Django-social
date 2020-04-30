from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from  django.urls import reverse
# Create your models here.
User=get_user_model()


class Post(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='post',blank=True)
    created_by=models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
    class Meta:
        ordering=['-created_at']





class Comment(models.Model):
    on_post=models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now())
    comment=models.TextField()



    def __str__(self):
        return self.comment[:30]
    class Meta:
        ordering=['-created_at']

    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'pk':self.on_post.pk})




