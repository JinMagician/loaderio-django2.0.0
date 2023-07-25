from django.urls import path
from loaderio.views import show_token


urlpatterns = [
    path(r'^(?P<token>loaderio-[0-9a-z]+)(?:\.txt|\.html|/)?$',
        show_token)
]
