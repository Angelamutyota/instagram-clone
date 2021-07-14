from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('register/', views.registerPage, name= 'register'),
   path('login/', views.loginPage, name= 'login'),
   path('logout/',views.logoutpage,name='logout'),

   path('', views.welcome, name='index'),
   path('comment/<int:id>',views.comments,name="comments"),
   path('new/image/', views.upload_image, name='new-image'),
   path('profile/',views.profile,name='profile'),
   path('search/',views.search_profile,name='search_results'),
   path('comments/',views.comments,name='comments')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)