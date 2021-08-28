from django.urls import path

from polls import views
from polls.views import index

urlpatterns = [
    path('', index),
    path('<int:p_id>', views.person_id),
]
