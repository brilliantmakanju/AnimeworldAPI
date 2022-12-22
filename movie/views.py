# from .util import send_mail
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from movie.models import Movies, Season, Episode
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_bytes, force_str, smart_str, DjangoUnicodeDecodeError
from movie.serializers import MovieSerilizers, SeasonSerilizers, EpisodeSerilizers, RegisterSerializer


@api_view(["GET"])
def Home(request):
    movies = Movies.objects.all()
    movie = MovieSerilizers(movies, many=True)
    return Response(movie.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def Seasons(request):
    seasons = Season.objects.all()
    season = SeasonSerilizers(seasons, many=True)
    return Response(season.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def Episodes(request):
    episodes = Episode.objects.all()[:20]
    episode = EpisodeSerilizers(episodes, many=True)
    return Response(episode.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def TopAnime(request):
    episodes = Episode.objects.order_by("-views")[:10]
    episode = EpisodeSerilizers(episodes, many=True)
    return Response(episode.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def LoginUsers(request):
    pass


@api_view(["POST"])
def Register_User(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    return Response({
        "Success": "You Registered Successfully"
    })


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
