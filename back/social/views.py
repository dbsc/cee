from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.test import APIClient
import requests


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:8000/social/google/login/callback/'

import google_auth_oauthlib


@api_view(['GET'])
def google_callback(request):
    try:
        code = request.query_params.get('code')
    except KeyError:
        Response(status=401)
    url = 'http://localhost:8000/social/google/login/'
    data = {"code": code}
    print(data)
    response = requests.post(url=url, data=data)

    # flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    #     'client_secret.json',
    #     scopes=['openid'],
    #     redirect_uri='http://localhost:8000/api/auth/google/callback/'
    # )
    # auth_url, state = flow.authorization_url(prompt='consent')
    # flow.fetch_token(code=code)
    # credentials = flow.credentials
    # return Response(credentials.token)
    # return(Response(response.status_code))
    access_token = dict(response.json())['access_token']
    return Response(access_token)
