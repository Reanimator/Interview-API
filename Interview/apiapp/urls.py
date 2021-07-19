from django.urls import path

from .views import AdminAddInterviewsView
from .views import AdminModInterviewsView
from .views import AdminReadAddQuestionsView
from .views import AdminModQuestionsView
from .views import AnonInterviewsView
from .views import AnonInterviewsAnswerView
from .views import AnonDetailsView

urlpatterns = [
    path('admin_add_interview/', AdminAddInterviewsView.as_view()),
    path('admin_mod_interview/<str:name>/', AdminModInterviewsView.as_view()),
    path('admin_read_question/', AdminReadAddQuestionsView.as_view()),
    path('admin_mod_question/<int:pk>/', AdminModQuestionsView.as_view()),
    path('anon_read_interview_list/', AnonInterviewsView.as_view()),
    path('anon_interview_answer/', AnonInterviewsAnswerView.as_view()),
    path('anon_interview/<int:id>/', AnonDetailsView.as_view()),
]
