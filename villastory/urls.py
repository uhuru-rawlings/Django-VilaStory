from django.contrib import admin
from django.urls import path
from signups.views import signup_view,signup_meth
from logins.views import login_view,login_meth
from profiles.views import profile_view,logout_view,savebio_view,addpost_view,addpostimages_view
from posts.views import post_view
from django.contrib.staticfiles.urls import static
from . import settings
from posts.views import addinfo_view
from searchitems.views import searchitems_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name="login"),
    path('signin',login_meth, name="signin"),
    path('signup/',signup_view, name="signup"),
    path('addinfo/',addinfo_view, name="addinfo"),
    path('searchitems/',searchitems_view, name="searchitems"),
    path('create_account/',signup_meth, name="create_account"),
    path('home/',post_view, name="homepage"),
    path('profile/',profile_view, name="profile"),
    path('create_posts/',addpost_view, name="create_posts"),
    path('createimage_posts/',addpostimages_view, name="createimage_posts"),
    path('save_bio/',savebio_view, name="save_bio"),
    path('logout/',logout_view, name="logout"),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
