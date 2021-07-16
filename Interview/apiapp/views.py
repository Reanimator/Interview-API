from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import AdminAddInterviewsSerializer
from .serializers import QuestionsSerializer

from .models import Interviews


class AdminAddInterviewsView(APIView):
    """Получение списка всех опросов"""
    def get(self, request):
        queryset = Interviews.objects.all()
        serializer = AdminAddInterviewsSerializer(queryset, many=True)
        return Response(serializer.data)

    """Добавление опросов"""
    def post(self, request):
        data = request.data
        serializer = AdminAddInterviewsSerializer(data=data)

        if serializer.is_valid(raise_exception=True):

            try:
                serializer.save()
                return Response({"success": f"Interview created successfully - {dict(data)}"})
            except:
                return Response({"fail": "Name  already exists"})


class AdminDelInterviewsView(APIView):
    """Изменение опросов"""
    def patch(self, request, name):

        try:
            queryset = Interviews.objects.get(name=name)
        except:
            return Response({"fail": f"not found - {name}"})

        serializer = AdminAddInterviewsSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"success": f"Interview created successfully - {serializer.data}"})
        return Response({"fail": {serializer.data}})

    """Удаление опросов"""
    def delete(self, request, name):

        try:
            queryset = Interviews.objects.get(name=name)
        except:
            return Response({"fail": f"not found - {name}"})

        queryset.delete()
        return Response({"success": f"Article created successfully"})


class AdminAddQuestionsView(APIView):
    """Получение списка всех вопросов"""
    def get(self, request):
        return Response({"success": f""})

    """Добавление вопросов"""
    def post(self, request):
        return Response({"success": f""})

class AdminDelQuestionsView(APIView):
    """Изменение вопросов"""
    def patch(self, request):
        return Response({"success": f""})

    """Удаление вопросов"""
    def delete(self, request):
        return Response({"success": f""})


class AnonInterviewsView(APIView):
    permission_classes = [AllowAny]
    """Получение списка опросов"""
    def post(self, request):
        return Response({"success": f""})


class AnonInterviewsDetailView(APIView):
    permission_classes = [AllowAny]
    """Получение опросов пользователя"""
    def post(self, request):
        return Response({"success": f""})


class AnonQuestionsView(APIView):
    permission_classes = [AllowAny]
    """Получение вопросов по опросу"""
    def get(self, request):
        return Response({"success": f""})

    """Отправка ответов пользователя"""
    def post(self, request):
        return Response({"success": f""})
