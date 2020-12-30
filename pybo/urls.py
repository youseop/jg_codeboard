from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

app_name = 'pybo'

urlpatterns = [
    # baes_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),


    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),


    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),


    #comment_views.py
    
]