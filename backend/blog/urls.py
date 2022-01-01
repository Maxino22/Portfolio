from django.urls import path, include
from . import views


urlpatterns = [
    # html routes
    path('', views.posts),
    path('blog/<str:post_slug>/', views.post),
    # api endpoints
    path('profile/', views.Profile.as_view()),
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetails.as_view()),
    path('contacts/', views.ContactView.as_view()),

]
