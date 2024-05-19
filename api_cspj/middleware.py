from django.http import HttpResponseForbidden

def restrict_access_middleware(get_response):
    def middleware(request):
        # Replace 'kong-proxy-ip' with the actual IP address of your Kong proxy
        if request.META.get('HTTP_X_FORWARDED_HOST') != '192.168.226.129':
            return HttpResponseForbidden('Access Denied')
        return get_response(request)
    return middleware