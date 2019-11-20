from rest_framework import routers
from django.urls import include, path

from . import views

app_name = 'EOTRTS'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'^student/{student_id}/$', views.StudentInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student/<str:student_id>/', views.student_information),

]
