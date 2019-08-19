from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(),name="homepage"),
    path('gettask/',views.GetAllTasks.as_view() ,name="gettask"),
    path('<int:pk>/markasdone/',views.MarkAsDone.as_view() ,name="markasdone"),
    path('<int:pk>/markaspending/',views.MarkAsPending.as_view() ,name="markaspending"),
    path('<int:pk>/updatetask/',views.UpdateTask.as_view() ,name="updatetask"),
]
