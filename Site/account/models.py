from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

#AboutUser details
class About(models.Model):
    user=models.OneToOneField(User,related_name='AboutUser',on_delete=models.CASCADE)#this user will contain user object
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=100,blank=True,default='')
    last_name=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='account')


    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('account:user_detail',kwargs={'pk':self.pk})
