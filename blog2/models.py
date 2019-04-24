from django.db import models

from django.contrib.auth.models import User

class blog2(models.Model):
    #user= models.ForeignKey(User,on_delete=models.CASCADE)
    usr_nm = models.CharField(max_length=100)
    usr_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'blog2'

    def __unicode__(self):
        return u"%s's users Info" % self.user_rec
