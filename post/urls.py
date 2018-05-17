from django.conf.urls import url
from django.urls import include, path
from .views import *
app_name='post'
urlpatterns = [
    
    path('index/',post_index,name='index'),
    path('<int:id>/detail/',post_detail,name='detail'),
    path('create/',post_create,name='create'),
    path('<int:id>/update/',post_update,name='update'),
    path('<int:id>/delete/',post_delete,name='delete'),

]
