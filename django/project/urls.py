from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from home import views as home_views

urlpatterns = [ 
    path('', home_views.home),
    path('blog/', blog_views.blog),
    path('admin/', admin.site.urls),
]
