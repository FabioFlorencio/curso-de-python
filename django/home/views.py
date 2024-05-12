from django.http import HttpResponse

def home(request):
    print('home')
    return HttpResponse('home now!')
