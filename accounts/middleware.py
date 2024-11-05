# middleware.py

from django.http import HttpResponseForbidden
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return self.get_response(request)
# middleware.py

class IPWhitelistMiddleware:
    ALLOWED_IPS = ['192.168.240.77']  # Replace with your allowed IPs

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Your IP is not allowed.")
        return self.get_response(request)
