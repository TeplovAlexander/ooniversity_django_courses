"""
local_settings.py
_________________

SECRET_KEY
DEBUG, TEMPLATE_DEBUG
ALLOWED_HOSTS
ADMINS, MANAGERS
EMAIL_BACKEND
EMAIL_HOST, EMAIL_PORT, EMAIL_...
DATABASES, CACHES, LOGGING
MEDIA_ROOT, STATIC_ROOT

"""

# Local settings for installation

SECRET_KEY = 'real-secret-key'

DEBUG = False	# False True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1']	# ['your-site.com']

