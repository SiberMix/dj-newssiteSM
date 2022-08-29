from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from news.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]
#Проверка на дебаг сайта для загрузки изображений
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)