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
    rank=models.IntegerField(default=0,blank=True)#rank of displaying on website

    def __str__(self):
        return self.first_name+" "+self.last_name

class alumni(models.Model):
    name=models.CharField(max_length=100)
    remark=models.CharField(max_length=100)#batch & position, like 2020-21 President
    experience=models.TextField()
    valid=models.BooleanField(default=False,blank=True)#to be kept on website or not
    rank=models.IntegerField(default=0,blank=True)#rank of displaying on website

    def __str__(self):
        return self.name

    
