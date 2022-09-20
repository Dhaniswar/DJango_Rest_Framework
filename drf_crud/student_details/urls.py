from django.urls import  re_path
from student_details import views
from .views import StudentList

urlpatterns = [
    re_path('', StudentList.as_view(), name="Student-List" ),
]
