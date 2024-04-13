from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blogCEO'),
    path('<int:pid>/', views.post_detail, name = 'post_detail'),
    path('new-post/', views.post_new, name = 'post_new'),
    
]