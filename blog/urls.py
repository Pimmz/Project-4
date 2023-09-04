from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.HomeView.as_view(), name='index'),
    # path('accounts/', include('allauth.urls')),
    path('posts', views.PostList.as_view(), name='blog'),
    path("adoption/", views.AdoptionView.as_view(), name='adoption'),
    path("rehome/", views.RehomeView.as_view(), name='rehome'),
    path("adoption/<int:pk>/", views.AdoptionDetailView.as_view(), name='adoption_detail'),
    path("update/<int:pk>/", views.AdoptionUpdateView.as_view(), name='update_adoption'),
    path("rehome/<int:pk>/", views.RehomeDetailView.as_view(), name='rehome_detail'),
    path("about/", views.AboutView.as_view(), name='about'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    
   
]
