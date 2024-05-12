from django.http import HttpResponse

def blog(request):
    print('blog')
    return HttpResponse('App blog 555')
