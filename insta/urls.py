from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.welcome, name='index'),
   path('comment/<int:id>',views.comments,name="comments"),
   path('new/image/', views.upload_image, name='new-image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)