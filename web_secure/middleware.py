import re

from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class WebSecureMiddleware:

    def __init__(self):
        self.enforce_ssl = settings.SECURE_ENFORCE_SSL
        self.ssl_host = settings.SECURE_SSL_HOST
        self.exempt_hosts = [re.compile(r) for r in settings.SECURE_EXEMPT_HOSTS]

        self.hsts_include_subdomains = settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
