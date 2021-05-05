from django.db import models

# Create your models here.
class member(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    board=models.CharField(max_length=50)       #main, asst, member
    position=models.CharField(max_length=50)    #event dir, treasure, etc
    team=models.CharField(max_length=50)        #dance, band, etc
    photo=models.URLField(max_length=100)                   
    description=models.CharField(max_length=200,blank=True)#hobbies, beliefs
    insta=models.URLField(blank=True)           #link to insta account
    artwork=models.CharField(max_length=100,blank=True)#blogs, art channel, etc
    artworklink=models.URLField(blank=True)     #link to above artwork
    valid=models.BooleanField(default=False,blank=True)#currently member or not

    def __str__(self):
        return self.first_name+self.last_name
    
