from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('current/', views.current_todos, name='current_todos'),
    path('completed/', views.completed_todos, name='completed_todos'),
    path('new/', views.create_todo, name='create_todo'),

    path('<int:todo_id>/', views.view_todo, name='view_todo'),
    path('<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('<int:todo_id>/complete/', views.complete_todo, name='complete_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
]

