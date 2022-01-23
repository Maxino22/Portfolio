from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemap import BlogSitemap
from django.views.generic.base import TemplateView



sitemaps = {
    'blogs': BlogSitemap
}

urlpatterns = [
    # html routes
    #  path('', views.home ),
     path('', views.posts, name='posts'),
     path('posts/<str:post_slug>/', views.post, name='post'),
    # api endpoints
    path('profile/', views.Profile.as_view()),
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetails.as_view()),
    path('contacts/', views.ContactView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),  
]
