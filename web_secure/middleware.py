from django.conf import settings


class WebSecureMiddleware:

    def __init__(self):
        self.enforce_ssl = settings.SECURE_ENFORCE_SSL
        self.hsts_seconds = settings.SECURE_HSTS_SECONDS
        self.hsts_include_subdomains = settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
