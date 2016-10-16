from django.shortcuts import render,get_object_or_404
from .models import Tags,Image
from searchengine.forms import QueryForm
import re
# Create your views here.
def index(request):
    image=None
    image_all=[]
    count=0
    if request.GET.get('search'):
        search = request.GET.get('search')
        search=re.findall('\w+',search)
        print "search",search
        image=Tags.objects.filter(tag_name__in=search).order_by('id').distinct()
        
        
        for i in image:
            image=image.distinct()
            
            for j in i.image_list():
                if j not in image_all:
                    image_all.append(j)
        count=len(image_all)
        
    return render(request,'searchengine/index.html',{'image':image_all,'count':count})

def tagDetails(request,tag_name):
    
    tag=get_object_or_404(Tags,tag_name)
    return render(request,'searchengine/tags.html',{'tag':tag})
def imageDetails(request,id):
    image=get_object_or_404(Image,pk=id)
    return render(request,'searchengine/image.html',{'image':image})
