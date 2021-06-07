from django.urls import path, include
from .views import GoogleLogin, google_callback

urlpatterns = [
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
    # path('auth/google/callback/', GoogleCallbackView.as_view(), name='callback')
    path('google/login/callback/', google_callback, name='callback')
]
