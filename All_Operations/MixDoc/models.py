from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class contact(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    message = models.CharField(max_length=150)
    
    def __str__(self):
        return self.email
    

class webcard(models.Model):
    cardname = models.CharField(max_length=50)
    cardpic = models.ImageField(upload_to='static/images/',default="")
    cardlink = models.CharField(max_length=500)
    
    def __str__(self):
        return self.cardname
    
    
class youTube(models.Model):
    video = models.CharField(max_length=500)
    vtitle = models.CharField(max_length=100)
    vdiscription = models.CharField(max_length=500)
    vchannel = models.CharField(max_length=50)
    vuploaded = models.CharField(max_length=50)
    vlink = models.CharField(max_length=500)
    
    def __str__(self):
        return self.video
    

class freeCard(models.Model):
    freeicon = models.ImageField(upload_to='static/images/',default="")
    freetitle = models.CharField(max_length=30)
    freelink = models.CharField(max_length=500)
    
"""  
class videoGallery(models.Model):
    youtubevideo = models.CharField(max_length=500)
    videotitle = models.CharField(max_length=100)
    videodiscp = models.CharField(max_length=200)
    videochannel = models.CharField(max_length=30)
    videotime = models.CharField(max_length=20)
    videolink = models.CharField(max_length=500)"""
    

class os(models.Model):
    os_img = models.ImageField(upload_to='static/images/',default="")
    os_title = models.CharField(max_length=30)
    os_discription = models.CharField(max_length=100)
    os_moreinfo = models.CharField(max_length=200)
    os_download = models.CharField(max_length=500)
    
    
class os1(models.Model):
    os_img1 = models.ImageField(upload_to='static/images/',default="")
    os_title1 = models.CharField(max_length=30)
    os_discription1 = models.CharField(max_length=100)
    os_moreinfo1 = models.CharField(max_length=200)
    os_download1 = models.CharField(max_length=500)
    
    
class os2(models.Model):
    os_img2 = models.ImageField(upload_to='static/images/',default="")
    os_title2 = models.CharField(max_length=30)
    os_discription2 = models.CharField(max_length=100)
    os_moreinfo2 = models.CharField(max_length=200)
    os_download2 = models.CharField(max_length=500)
    
STATE_CHOICE = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar haveli','Dadra & Nagar haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('haryana', 'haryana'),
    ('Himchal Pradesh','Himchal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkand','Jharkand'),
    ('Karnataka','Karnataka'),
    ('Kerla','Kerla'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Naidu','Tamil Naidu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    
)
  
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='static/images/', blank=True)
    my_file = models.FileField(upload_to='static/doc/', blank=True)
 

class templateResume(models.Model):
    temp_pic = models.ImageField(upload_to='static/images/', default="")
    temp_download = models.FileField(upload_to='static/doc/', blank=True)    
    
class newscard(models.Model):
    newsname = models.CharField(max_length=80)
    newspic = models.ImageField(upload_to='static/images/',default="")    
    newslink = models.CharField(max_length=500)
    
    def __str(self):
        return self.newslink
    
class newscard1(models.Model):
    newsname1 = models.CharField(max_length=80)
    newspic1 = models.ImageField(upload_to='static/images/',default="")    
    newslink1 = models.CharField(max_length=500)
    
    def __str(self):
        return self.newslink1
    
class newscard2(models.Model):
    newsname2 = models.CharField(max_length=80)
    newspic2 = models.ImageField(upload_to='static/images/',default="")    
    newslink2 = models.CharField(max_length=500)
    
    def __str(self):
        return self.newslink2
    
class newscard3(models.Model):
    newsname3 = models.CharField(max_length=80)
    newspic3 = models.ImageField(upload_to='static/images/',default="")    
    newslink3 = models.CharField(max_length=500)
    
    
class newscard4(models.Model):
    newsname4 = models.CharField(max_length=80)
    newspic4 = models.ImageField(upload_to='static/images/',default="")    
    newslink4 = models.CharField(max_length=500)
    