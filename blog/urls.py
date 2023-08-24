from . import views
from django.urls import path, include

urlpatterns = [
    path("index/", views.HomeView.as_view(), name='index'),
    # path('accounts/', include('allauth.urls')),
    path('', views.PostList.as_view(), name='blog'),
    path("adoption/", views.AdoptionView.as_view(), name='adoption'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
