from django.contrib import admin
from .models import Resume
# Register your models here.
from .models import *


class contactusAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email","number","message")
admin.site.register(contact,contactusAdmin)


class webcardAdmin(admin.ModelAdmin):
    list_display = ("id", "cardname", "cardpic", "cardlink")
admin.site.register(webcard,webcardAdmin)


class youTubeAdmin(admin.ModelAdmin):
    list_display = ("id", "video","vtitle", "vdiscription", "vchannel", "vuploaded", "vlink")
admin.site.register(youTube,youTubeAdmin)


class freeCardAdmin(admin.ModelAdmin):
    list_display = ("id", "freeicon", "freetitle", "freelink")
admin.site.register(freeCard,freeCardAdmin)


"""class videoGalleryAdmin(admin.ModelAdmin):
    list_display = ("youtubevideo","videotitle", "videodiscp", "videochannel", "videotime", "videolink")
admin.site.register(videoGallery,videoGalleryAdmin)"""


class osAdmin(admin.ModelAdmin):
    list_display = ("id", "os_img", "os_title", "os_discription", "os_moreinfo", "os_download")
admin.site.register(os,osAdmin)


class os1Admin(admin.ModelAdmin):
    list_display = ("id", "os_img1", "os_title1", "os_discription1", "os_moreinfo1", "os_download1")
admin.site.register(os1,os1Admin)


class os2Admin(admin.ModelAdmin):
    list_display = ("id", "os_img2", "os_title2", "os_discription2", "os_moreinfo2", "os_download2")
admin.site.register(os2,os2Admin)


@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality',
    'city', 'pin', 'state', 'mobile', 'job_city', 
    'profile_image','my_file']
    
    
class newscardAdmin(admin.ModelAdmin):
    list_display = ("id", "newsname", "newspic", "newslink")
admin.site.register(newscard,newscardAdmin)    

class newscard1Admin(admin.ModelAdmin):
    list_display = ("id", "newsname1", "newspic1", "newslink1")
admin.site.register(newscard1,newscard1Admin)    

class newscard2Admin(admin.ModelAdmin):
    list_display = ("id", "newspic2", "newsname2", "newslink2")
admin.site.register(newscard2,newscard2Admin)

class newscard3Admin(admin.ModelAdmin):
    list_display = ("id", "newspic3", "newsname3", "newslink3")
admin.site.register(newscard3,newscard3Admin)

class newscard4Admin(admin.ModelAdmin):
    list_display = ("id", "newspic4", "newsname4", "newslink4")
admin.site.register(newscard4,newscard4Admin) 

class templateResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "temp_pic", "temp_download")
admin.site.register(templateResume,templateResumeAdmin)
