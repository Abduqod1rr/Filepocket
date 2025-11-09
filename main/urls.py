from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("", views.Home.as_view(), name="home"),
    path("register/", views.registerview.as_view(), name="register"),
    path("login/", views.userlogin.as_view(), name="login"),
    path("logout/", views.userlogout, name="logout"),
    path("upload/", views.uploadfile.as_view(), name="upload_file"),
    path("delete/<int:pk>", views.deletefile.as_view(), name="delete_file")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
