"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import splash, user_login, logout_, signup_, Feed, create_post, get_hashtag, get_user_profile, delete_post, LikeView

app_name = 'main'

urlpatterns = [
    path('admin', admin.site.urls),
	path('', splash, name='splash'),
    path('login', user_login, name='login'),
    path('logout', logout_, name='logout'),
    path('signup', signup_, name='signup'),
    path('feed', Feed.as_view(), name='feed'),
    path('feed/<str:hashtag>', get_hashtag, name='hashtag'),
    path('posts', create_post, name = 'posts'),
    path('<str:username>', get_user_profile, name='profile'),
    path('delete/<post_id>', delete_post, name='delete'),
    path('like/<post_id>', LikeView, name='like_post')
]
