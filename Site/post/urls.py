from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='post'
urlpatterns=[
    path('list/',PostList.as_view(),name='post_list'),
    path('create_post/',CreatePost.as_view(),name='create_post'),
    path('comment/<int:pk>/',commentCreate,name='comment'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('delete_post/<int:pk>/',DeletePost.as_view(),name='delete_post'),
   # path('delete_comment/<int:pk>/',DeleteComment.as_view(),name='delete_comment'),
    path('delete_comment/<int:pk>/',deleteCommment,name='delete_comment'),
    #path('post_edit/<int:pk>/',UpdatePost.as_view(),name='update_post'),
    #path('comment_edit/<int:pk>/',UpdateComment.as_view(),name='update_comment'),
    path('editpost/<int:pk>/',EditPost.as_view(),name='edit_post'),
    path('editcomment/<int:pk>',EditComment.as_view(),name='edit_comment'),


]