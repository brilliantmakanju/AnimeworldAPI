from django.urls import path
from movie.views import (Home, Episodes, Seasons,
                         TopAnime, LoginUsers, MyTokenObtainPairView)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path("Home", Home, name="home"),
    path("Season", Seasons, name="season"),
    path("Eposide", Episodes, name="episode"),
    path("TopAnime", TopAnime, name="topAnime"),
    path("Login", LoginUsers, name="loginUsers"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair')
]
