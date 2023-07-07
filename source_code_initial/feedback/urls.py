from django.urls import path

from .views import FeedbackFormView, SuccessView, long_polling_view

app_name = "feedback"

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    path('long-polling/', long_polling_view, name='long_polling_endpoint'),
]
