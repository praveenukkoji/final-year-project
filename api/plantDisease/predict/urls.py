from django.urls import path
from predict.controller.controller import PredictImage

urlpatterns = [
    path('', PredictImage.as_view()),
]
