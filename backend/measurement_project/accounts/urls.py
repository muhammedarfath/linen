from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      
    
path('sign_up/',SignupView.as_view()),
path('login/', LoginView.as_view()),
path('logout/', LogoutView.as_view()),

]
                        