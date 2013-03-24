from django.db import models
import barcode
from django.contrib import admin

class Package(models.Model):

    package_tracking_number = models.CharField(max_length=200) 
    package_date_entered = models.DateTimeField()
    package_recipient = models.ForeignKey('Recipient')
    package_contents = models.CharField(max_length=200)
    special_insrtuctions = models.CharField(max_length=200) #Delete
    destination = models.CharField(max_length=200)
    package_current_location = models.CharField(max_length=200)
    def __unicode__(self):
        return self.package_tracking_number
    
    
class Recipient(models.Model):
    recip_username = models.CharField(max_length=20)
    recip_first_name = models.CharField(max_length=200)
    recip_last_name = models.CharField(max_length=200)
    recip_company = models.CharField(max_length=200)
    recip_city = models.CharField(max_length=200)
    recip_notes = models.CharField(max_length=200)
    recip_email = models.EmailField()
    recip_n_packages = models.IntegerField()
    def __unicode__(self):
        return self.recip_username
    



    
