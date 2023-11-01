from django.urls import path, include
from . import views
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
#  path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
 # API for UI
#  path('udops/create_corpus/', views.create_corpus.as_view()),
 path('viridium/pfas/prompt/', views.get_chunks)]