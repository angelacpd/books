from django.urls import path

from .views import SignupPageView


urlpatterns = [
    path('', SignupPageView.as_view(), name='signup'),
]
