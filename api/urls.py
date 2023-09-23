from django.urls import path
from api import views



urlpatterns = [
    path('generate/id', views.random_uuid, name='random-uuid'),
    path('chat/<uuid:chat_id>', views.prompt,name='chat_id'),
    path('conversation/<uuid:conv_id>', views.conversation,name='conv_id'),
    path('conversation/gen_title/<uuid:conv_id>', views.gen_title,name='conv_id'),
    
]
