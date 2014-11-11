import re

from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class WebSecureMiddleware:
    CONTENT_SECURITY_POLICY_HEADER = 'Content-Security-Policy'
    CONTENT_TYPE_OPTIONS_HEADER = 'X-Content-Type-Options'
    HSTS_HEADER = 'Strict-Transport-Security'
    XSS_PROTECTION_HEADER = 'X-XSS-Protection'

    def __init__(self):
        self.enforce_ssl = settings.SECURE_ENFORCE_SSL
        self.ssl_host = settings.SECURE_SSL_HOST
        self.exempt_hosts = [re.compile(r) for r in settings.SECURE_EXEMPT_HOSTS]

        self.hsts_max_age = settings.SECURE_HSTS_MAX_AGE
        self.hsts_include_subdomains = settings.SECURE_HSTS_INCLUDE_SUBDOMAINS
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

    def get_hsts_header(self):
        header = ''
        if self.hsts_max_age:
            header += 'max-age={}'.format(self.hsts_max_age)
            if self.hsts_include_subdomains:
                header += '; includesubdomains'
            if self.hsts_preload:
                header += '; preload'
        return header

    def process_response(self, request, response):
        if request.is_secure() and self.HSTS_HEADER not in response:
            response[self.HSTS_HEADER] = self.get_hsts_header()
        if self.content_type_nosniff and self.CONTENT_TYPE_OPTIONS_HEADER not in response:
            response[self.CONTENT_TYPE_OPTIONS_HEADER] = 'nosniff'
        if self.xss_filter and self.XSS_PROTECTION_HEADER not in response:
            response[self.XSS_PROTECTION_HEADER] = '1; mode=block'
        return response
