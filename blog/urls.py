"""Url Patterns"""
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.HomeView.as_view(), name='index'),
    path('posts', views.PostList.as_view(), name='blog'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path("update_post/<slug:slug>/",
         views.UpdatePostView.as_view(), name='update_post'),
    path('blog.html', views.PostList.as_view(), name='blog'),
    path("adoption/", views.AdoptionView.as_view(), name='adoption'),
    path("rehome/", views.RehomeView.as_view(), name='rehome'),
    path("adoption/<int:pk>/", views.AdoptionDetailView.as_view(),
         name='adoption_detail'),
    path("update_adoption/<int:pk>/",
         views.AdoptionUpdateView.as_view(), name='update_adoption'),
    path("delete_adoption/<int:pk>/",
         views.DeleteAdoptionView.as_view(), name='delete_adoption'),
    path("rehome/<int:pk>/", views.RehomeDetailView.as_view(), name='rehome_detail'),
    path("update_rehome/<int:pk>/",
         views.RehomeUpdateView.as_view(), name='update_rehome'),
    path("delete_rehome/<int:pk>/",
         views.DeleteRehomeView.as_view(), name='delete_rehome'),
    path("about/", views.AboutView.as_view(), name='about'),
    path('comment/<slug:slug>', views.PostComment.as_view(), name='post_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
