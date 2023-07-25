from django.urls import re_path
from loaderio.views import show_token


urlpatterns = [
    re_path(r'^(?P<token>loaderio-[0-9a-z]+)(?:\.txt|\.html|/)?$',
        show_token)
]
