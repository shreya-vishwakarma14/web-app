from re import template
from django import views
from django.shortcuts import render
from .models import *
from .forms import *

from django.views import *
from youtubesearchpython import VideosSearch
# Create your views here.

def home(request):
    return render(request, 'html_files/index.html')

def news(request):
    newsdata = newscard.objects.all()
    newsdata1 = newscard1.objects.all()
    newsdata2 = newscard2.objects.all()
    newsdata3 = newscard3.objects.all()
    newsdata4 = newscard4.objects.all()
    return render(request,'html_files/news.html',{'data':newsdata, 'tech':newsdata1, 'cbrnews':newsdata2, 'business':newsdata3, 'social':newsdata4})
 

def Os(request):
    osdata = os.objects.all()
    osdata1 = os1.objects.all()
    osdata2 = os2.objects.all()
    return render(request,'html_files/os.html',{"oscard" : osdata, "oscard1":osdata1, "oscard2":osdata2})

def contactus(request):
    status = False
    if request.method=='POST':
        Fname = request.POST.get("fullname","")
        Email = request.POST.get("email","")
        Number = request.POST.get("number","")
        Message = request.POST.get("message","")
        x = contact(fullname=Fname, email=Email, number=Number, message=Message)
        x.save()
        status=True
    return render(request,'html_files/contactus.html',{'S':status})

def courses(request):
    carddata = webcard.objects.all()
    freecard = freeCard.objects.all()
    return render(request,'html_files/courses.html',{"data":carddata, "free":freecard})


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        resumeTemp = templateResume.objects.all()
        return render(request,'html_files/resumes.html',{'candidates' :candidates,'form':form, 'resume':resumeTemp})
    
    def post(self,request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'html_files/resumes.html',{'form':form})
        

class candidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'html_files/candidate.html',{'candidate':candidate})


def videogallery(request):
    if request.method == 'POST':
        form = DashboradForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
            }
        return render(request,'html_files/videogallery.html',context)
    else:
        form = DashboradForm()
    context = {'form':form}
    #videodata = videoGallery.objects.all().order_by('id')[0:6]
    return render(request,'html_files/videogallery.html',context)



