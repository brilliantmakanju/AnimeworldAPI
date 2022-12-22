from django.contrib.auth.models import User
from movie.models import Movies, Season, Episode
from rest_framework import serializers, validators
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_bytes, force_str, smart_str, DjangoUnicodeDecodeError


class MovieSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['pk', 'title',
                  'genre', 'season', 'episode']


class SeasonSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['pk', 'title', 'views',
                  'thumbnail']


class EpisodeSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['pk', 'title', 'views',
                  'thumbnail', 'video']


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), "Username Taken"
                    )
                ]
            },
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), "Email Taken "
                    )
                ]
            }
        }

        def create(self, validated_data):
            email = validated_data.get('email')
            username = validated_data.get('username')
            password = validated_data.get('password')

            user = User.objects.create(
                username=username,
                password=password,
                email=email
            )

            return user
