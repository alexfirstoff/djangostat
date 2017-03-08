"""firstoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
#from article.views import basic_one, basic_two, basic_3, articles, addlike, article
from article.views import main_view, main_view_claster

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^claster/', main_view_claster),

    url(r'^', main_view)


    #url(r'^basicview/1', basic_one),
    #url(r'^basicview/2', basic_two),
    #url(r'^basicview/3', basic_3),
    #url(r'^add/(?P<article_id>\d+)/$', addlike),

    #url(r'^/add1', article),
]
