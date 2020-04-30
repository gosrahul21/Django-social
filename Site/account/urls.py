from django.urls import path
from account import views
from django.contrib.auth.views import LoginView,LogoutView
app_name='account'

urlpatterns=[
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('about/',views.AboutCreate.as_view(),name='about_create'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('userdetail/<int:pk>/',views.UserDetail.as_view(),name='user_detail'),
    path('updateUser/<int:pk>/',views.UpdateAccount.as_view(),name='userupdate'),

]