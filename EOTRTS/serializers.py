from django.contrib.auth.models import User, Group
from rest_framework import serializers

from EOTRTS.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StudentInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentData
        fields = ['student_id', 'student_name']


class StudentCourseProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseProgress
        fields = ['current_course']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
