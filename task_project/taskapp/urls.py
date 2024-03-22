from django.urls import path
from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.regiter, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-project/', views.add_project, name='add_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('update-task/<int:task_id>/', views.update_task_completion, name='update_task_completion'),
]