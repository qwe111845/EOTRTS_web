from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from EOTRTS.serializers import *
from EOTRTS_web.settings import BASE_DIR
from .models import StudentData
from rest_framework.response import Response
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


def student_information(request, student_id):
    try:
        if request.method == 'GET':
            student_inform = get_object_or_404(StudentData, student_id=student_id)
            serializer = StudentInformationSerializer(student_inform)

            return JsonResponse(serializer.data)
        else:
            pass
    except StudentData.DoesNotExist:
        return HttpResponse(status=404)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            request.FILES.get('filename')
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)