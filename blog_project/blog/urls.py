from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup-page'),
    path('user-profile/<str:user_name>/', views.profile, name="profile"),
    path('loginn/', views.loginn, name='login-page'),
    path('mypost/', views.myPost, name='my-post'),
    path('signout/', views.signout, name='signout-btn'),
    path('contact_us/', views.contactUs, name="contact_us"),
    path('blog_detail/<str:slug>', views.blog_detail, name='blog_detail'),
    path('CreateBlog', views.CreateBlog.as_view(), name='CreateBlog'),
    path('UpdateBlog/<int:pk>/', views.UpdateBlog.as_view(), name='UpdateBlog'),
    path('DeleteBlog/<int:pk>/', views.DeleteBlog.as_view(), name='DeleteBlog'),
    path('DeleteUser/<int:pk>/', views.DeleteUser.as_view(), name="DeleteUser"),
]