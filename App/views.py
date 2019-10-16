from django.shortcuts import render,HttpResponse
from App.models import Master
import time

# Create your views here.
ISOTIMEFORMAT='%Y-%m-%d'


def index(request):
    return HttpResponse("helloworld")

def one_data(request):
    data1 = Master(name='111',money='222',first_time=time.strftime(ISOTIMEFORMAT),number = '50')
    data1.save()
    return HttpResponse("添加成功")

def search_form(request):
    return render(request, 'search.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.POST and request.POST['q']:
        x = '你搜索的内容为'+request.POST['q']
    else:
         x = '你搜索的内容为空'
    return HttpResponse(x)

