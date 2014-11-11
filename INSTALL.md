**1)** Add `django_web_secure` in `settings.py`, INSTALLED_APPS:

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'django_web_secure',
)
```


**2)** Add `django_web_secure.middleware.WebSecureMiddleware` in `settings.py`, MIDDLEWARE_CLASSES

It must be added before `CommonMiddleware`!


```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django_web_secure.middleware.WebSecureMiddleware'

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
```

3) Add and set the following settings in `settings.py`:


* `SECURE_ENFORCE_SSL` = True/False (recommended True)
* `SECURE_SSL_HOST` = 'https://example.com' (recommended your HTTPS host)
* `SECURE_EXEMPT_HOSTS` = 'regex string' containing any malicious (according to you) hosts
* `SECURE_HSTS_MAX_AGE` = integer seconds (recommended `31536000` which equals 1 year).
* `SECURE_HSTS_INCLUDE_SUBDOMAINS` = True/False, if you want subdomains-wide HSTS
* `SECURE_HSTS_PRELOAD` = True/False, if you want to take advantage of HSTS preloading on Chrome and Firefox. However it requires some extra work, read more here ->  https://hstspreload.appspot.com/
* `SECURE_CONTENT_POLICY` = 'directives' as seen in w3's site, [here](http://www.w3.org/TR/CSP2/#sec-directives)
* `SECURE_CONTENT_TYPE_NOSNIFF` = True/False to prevent MIME-sniffing a response in most browsers.
* `SECURE_XSS_FILTER` = True/False to force enable Cross-site-scripting filter.



**4)** Restart your Django web app.
