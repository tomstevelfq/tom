from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/',views.detail),
    path('<int:question_id>/results/',views.results),
    path('<int:question_id>/vote/',views.vote),
    path('index/',views.index),
    path('vue/',views.vue),
]