from django.urls import path
from home import  views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.main,name='main'),
    path('api/',views.api,name='api')
]
#解决图片不能显示的问题
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

