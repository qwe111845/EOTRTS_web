from django.urls import path

from . import views

app_name = 'EOTRTS'


urlpatterns = [
    path('student/<str:student_id>/', views.student_information),
    path('upload/', views.FileUploadView.as_view())

]
