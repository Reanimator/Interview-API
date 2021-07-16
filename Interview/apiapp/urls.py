from django.urls import path

from .views import AdminAddInterviewsView
from .views import AdminDelInterviewsView
from .views import AdminAddQuestionsView

urlpatterns = [
    path('admin_add_interview/', AdminAddInterviewsView.as_view()),
    path('admin_del_interview/<str:name>/', AdminDelInterviewsView.as_view()),
    path('admin_add_question/', AdminAddQuestionsView.as_view()),
    path('admin_del_question/<str:name>/', AdminAddQuestionsView.as_view()),
]
