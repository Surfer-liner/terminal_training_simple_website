from django.urls import path
from . import views


app_name = 'simple_site'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic'),
    path('edit_comment/<int:comment_id>', views.edit_comment,
         name='edit_comment'),
]
