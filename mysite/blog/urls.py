from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #post views
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    #https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-converters
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]

#Creating a urls.py file for each application is the best way to make your applications reusable by other projects.
