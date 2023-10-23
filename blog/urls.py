"""Url Patterns"""
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.HomeView.as_view(), name='index'),
    path('posts', views.PostList.as_view(), name='blog'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(),
         name='delete_post'),
    path("update_post/<slug:slug>/",
         views.UpdatePostView.as_view(), name='update_post'),
    path('blog.html', views.PostList.as_view(), name='blog'),
    path("adoption/", views.AdoptionView.as_view(), name='adoption'),
    path("adoption/<int:pk>/", views.AdoptionDView.as_view(),
         name='adoption_detail'),
    path("update_adoption/<int:pk>/",
         views.AdoptionUpdateView.as_view(), name='update_adoption'),
    path("delete_adoption/<int:pk>/",
         views.DeleteAdoptionView.as_view(),
         name='delete_adoption'),
    path("about/", views.AboutView.as_view(), name='about'),
    path('comment/<slug:slug>', views.PostComment.as_view(),
         name='post_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('accounts/', include('allauth.urls')),
    path('400/', views.custom_400.as_view(), name='custom_400'),
    path('403/', views.custom_403.as_view(), name='custom_403'),
    path('404/', views.custom_404.as_view(), name='custom_404'),
    path('500/', views.custom_500.as_view(), name='custom_500'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
