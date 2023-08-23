from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    # path('accounts/', include('allauth.urls')),
    path("adoption/", views.AdoptionView.as_view(), name='adoption'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
