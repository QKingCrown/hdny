from django.shortcuts import render,HttpResponse
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

# def search(request):
#     request.encoding='utf-8'
#     if 'q' in request.GET and request.GET['q']:
#         x = '你搜索的内容为'+request.GET['q']
#     else:
#          x = '你搜索的内容为空'
#     return HttpResponse(x)