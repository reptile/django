from django.db import models

#import string
#import random
#def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
#    return ''.join(random.choice(chars) for x in range(size))

# Create your models here.
class Affmail(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(null=True,blank=True,unique=True,max_length=200)
    email = models.CharField(unique=True,max_length=200)
    affiliate_referencer_id = models.IntegerField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    unique_reference_code = models.CharField(null=True,blank=True,unique=True,max_length=8)
    #def __unicode__(self):
        #return self.email
