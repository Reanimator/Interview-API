from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import AdminInterviewsSerializer
from .serializers import QuestionsTypeSerializer
from .serializers import QuestionsFullSerializer
from .serializers import QuestionsTextSerializer
from .serializers import QuestionsVarSerializer
from .serializers import QuestionsMvarSerializer


from .models import Interviews
from .models import Questions


class AdminAddInterviewsView(APIView):
    """Получение списка всех опросов"""
    def get(self, request):
        queryset = Interviews.objects.all()
        serializer = AdminInterviewsSerializer(queryset, many=True)
        return Response(serializer.data)

    """Добавление опросов"""
    def post(self, request):
        try:
            Interviews.objects.get(name=dict(request.data)['name'][0])
            return Response(status=400, data={"fail": "Name already exists"})
        except:
            pass

        serializer = AdminInterviewsSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201, data={"success": f"Interview created successfully - {dict(request.data)}"})


class AdminModInterviewsView(APIView):
    """Изменение опросов"""
    def patch(self, request, name):

        try:
            queryset = Interviews.objects.get(name=name)
        except:
            return Response(status=400, data={"fail": f"not found - {name}"})

        serializer = AdminInterviewsSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.update(queryset, serializer.validated_data)
            return Response(status=200, data={"success": f"Interview update successfully - {serializer.data}"})
        return Response(status=400, data={"fail": serializer.data})

    """Удаление опросов"""
    def delete(self, request, name):

        try:
            queryset = Interviews.objects.get(name=name)
        except:
            return Response(status=400, data={"fail": f"not found - {name}"})

        queryset.delete()
        return Response(status=200, data={"success": f"Article deleted"})


class AdminReadAddQuestionsView(APIView):
    """Получение списка всех вопросов"""
    def get(self, request):
        queryset = Questions.objects.all()
        serializer = QuestionsFullSerializer(queryset, many=True)
        return Response(serializer.data)

    """Добавление вопросов"""
    def post(self, request):
        serializer = QuestionsTypeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer_type = serializer.data["question_type"]
            if serializer_type == "text":
                serializer = QuestionsTextSerializer(data=request.data)
            elif serializer_type == "1var":
                serializer = QuestionsVarSerializer(data=request.data)
            elif serializer_type == "mvar":
                serializer = QuestionsMvarSerializer(data=request.data)
            else:
                return Response(status=400, data={"fail": "type not found"})

            if serializer.is_valid(raise_exception=True):
                print(serializer.validated_data)
                serializer.save()
                return Response(status=200, data={"success": f"Interview created successfully"})
            return Response(status=400, data={"fail": f"not found"})


class AdminModQuestionsView(APIView):
    """Изменение вопроса"""
    def patch(self, request, pk):

        try:
            queryset = Questions.objects.get(pk=pk)
        except:
            return Response(status=400, data={"fail": f"not found - {pk}"})

        serializer = QuestionsTypeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer_type = serializer.data["question_type"]
            if serializer_type == "text":
                serializer = QuestionsTextSerializer(data=request.data)
            elif serializer_type == "1var":
                serializer = QuestionsVarSerializer(data=request.data)
            elif serializer_type == "mvar":
                serializer = QuestionsMvarSerializer(data=request.data)
            else:
                return Response(status=400, data={"fail": "type not found"})

        if serializer.is_valid():
            serializer.update(queryset, serializer.validated_data)
            return Response(status=200, data={"success": f"Interview update successfully - {serializer.data}"})
        return Response(status=400, data={"fail": serializer.data})

    """Удаление вопроса"""
    def delete(self, request, pk):

        try:
            queryset = Questions.objects.get(pk=pk)
        except:
            return Response(status=400, data={"fail": f"not found - {pk}"})

        queryset.delete()
        return Response(status=200, data={"success": f"Article deleted"})







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
