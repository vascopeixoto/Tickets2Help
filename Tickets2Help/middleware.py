from django.conf import settings
from django.shortcuts import redirect


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == settings.LOGIN_URL and request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return self.get_response(request)