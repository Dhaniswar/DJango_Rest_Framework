from django.urls import urls
from .views import StudentList

urlpatterns = [
    path('', StudentList.as_view(), name="Student-List" ),
]
