from django.shortcuts import HttpResponseRedirect
from django.conf import settings

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if path not in ["account/login/", "admin/"]:
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            path = request.path_info.lstrip('/')
            if path in "account/login/":
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        # Code to be executed for each request/response after
        # the view is called.

        return response
