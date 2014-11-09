import re

from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class WebSecureMiddleware:

    def __init__(self):
        self.enforce_ssl = settings.SECURE_ENFORCE_SSL
        self.ssl_host = settings.SECURE_SSL_HOST
        self.exempt_hosts = [re.compile(r) for r in settings.SECURE_EXEMPT_HOSTS]

        self.hsts_include_subdomains = settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
        self.hsts_max_age = settings.SECURE_HSTS_MAX_AGE
        self.hsts_preload = settings.SECURE_HSTS_PRELOAD

        self.content_security_policy = settings.SECURE_CONTENT_POLICY
        self.content_type_nosniff = settings.SECURE_CONTENT_TYPE_NOSNIFF
        self.xss_filter = settings.SECURE_XSS_FILTER

    def is_exempt(self, path):
        return any(pattern.search(path) for pattern in self.exempt_hosts)

    def process_request(self, request):
        if self.enforce_ssl is None:
            return None
        elif self.enforce_ssl and not request.is_secure():
            path = self.ssl_host.lstrip('/')
            if not self.is_exempt(path):
                host = self.ssl_host or request.get_host()
                path = request.get_full_path()
                return HttpResponsePermanentRedirect('https://{0}{1}'.format(host, path))
