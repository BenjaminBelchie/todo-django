from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.home, name='todo-home'),
    path('add', views.addTodo, name='addTodo'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deleteComplete', views.deleteCompleted, name='deleteComplete'),
    path('deleteall', views.deleteAll, name='deleteAll'),
    path('create/',views.create, name='create'),

]