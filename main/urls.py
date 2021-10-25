from django.urls import path
from .import views

app_name="main"

urlpatterns = [
    path('',views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addproject/',views.add_project , name="add_project"),
    path('editproject/<int:id>/',views.edit_project, name="edit_project"),
    path('deleteproject/<int:id>/', views.deleteproject, name="deleteproject"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:project_id>/<int:review_id>/',views.edit_review, name="edit_review"),
    path('deletereview/<int:project_id>/<int:review_id>/',views.delete_review, name="delete_review")
]
