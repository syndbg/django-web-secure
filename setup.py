import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-web-secure',
    version='0.1',
    packages=['django_web_secure'],
    install_requires=["Django>=1.6.0"],
    include_package_data=True,
    license='MIT',
    description='The middleware that makes ponies fly with a great sense of security.',
    long_description=README,
    url='https://github.com/syndbg/django-web-secure',
    author='Anton Antonov',
    author_email='syndbe@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    platforms='any',
    keywords='pypi django web security secure package',
)
