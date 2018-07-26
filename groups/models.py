from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from accounts.models import User

#import misaka  # TEMPORARILY C-OUT 

from django.contrib.auth import get_user_model  # return the user model that is currently active in this project
User = get_user_model()  # create a user object

# This is for the in_group_members check template tag

from django import template
register = template.Library()   # check 

class Group(models.Model): # hereda de models.Model
    #atributos
    name = models.CharField(max_length=255, unique=True) # para q no se overlap names
    slug = models.SlugField(allow_unicode=True, unique=True) 
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True) # no useful by now 
    members = models.ManyToManyField(User,through="GroupMember")

    #methods
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #self.description_html = misaka.html(self.description)  #TEMPORARILY C-OUT
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug}) # basically a dictionary

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name='memberships') #the model to map to. / I need the on_delete argument
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_groups')

    def __str__(self): # str representation of this object
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
