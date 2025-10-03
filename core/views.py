from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer


# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Register View (for new users)
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if User.objects.filter(username=data.get("username")).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            password=make_password(data.get("password"))
        )
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)