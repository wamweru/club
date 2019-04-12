from django.urls import path
from .import views
app_name = "classes"

urlpatterns=[
    path('login', views.signin, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('?P<club_id>[0-9]+)/', views.detail, name='detail'),
    path('new_club', views.create_club, name='new_club'),
    path('?P<club_id>[0-9]+)/new_student', views.create_student, name='new_student'),
    path('?P<club_id>[0-9]+)/delete_club', views.delete_club, name='delete_club'),
    path('<int:pk>/update_club', views.ClubUpdateView.as_view(), name='update_club'),
    path('?P<club_id>[0-9]+)/delete_student/(?P<student_id>[0-9]+)/', views.delete_student, name='delete_student'),
    path('<int:pk>/update_student', views.StudentUpdateView.as_view(), name='update_student'),

]