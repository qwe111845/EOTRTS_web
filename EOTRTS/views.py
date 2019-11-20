from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets
from EOTRTS.serializers import UserSerializer, GroupSerializer, StudentInformationSerializer
from .models import StudentData
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@csrf_exempt
class StudentInformationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = StudentData.objects.all()

    @action(detail=False)
    def get_student_information(self, request, student_id=None):

        try:
            data = StudentData.objects.get(student_id=student_id)
        except StudentData.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = StudentInformationSerializer(data)
            return JsonResponse(serializer.data)


def student_information(request, student_id):
    try:
        if request.method == 'GET':
            student_inform = get_object_or_404(StudentData, student_id=student_id)
            serializer = StudentInformationSerializer(student_inform)
            return JsonResponse(serializer.data)

        else:
            serializer = ""
    except StudentData.DoesNotExist:
        return HttpResponse(status=404)


