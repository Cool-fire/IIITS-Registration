"""fblogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from allauth.account.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from upload import views as upload_views
from auth import views as a_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),


url(r'^signup/',a_views.signup,name="signup"),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/',auth_views.login,{'template_name':'allauth/account/login.html'},name="login"),


    url(r'^home/',views.home,name="home"),
    url(r'^index/',views.index,name ="index"),

    url(r'^$',views.ind,name = "ind"),
    url(r'^upload/',upload_views.list,name="list"),

    url('^',include('django.contrib.auth.urls')),
    url(r'^password_reset/', auth_views.password_reset,name='reset_password'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,name='password_Reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.password_reset_confirm),
    url(r'^reset/done/$', auth_views.password_reset_complete),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
