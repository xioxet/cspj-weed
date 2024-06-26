from django.http import HttpResponseForbidden

def restrict_access_middleware(get_response):
    def middleware(request):
        # Replace 'kong-proxy-ip' with the actual IP address of your Kong proxy
        if request.META.get('REMOTE_ADDR') != '127.0.0.1':
            print(request.META)
            return HttpResponseForbidden(f'Access Denied {request.META}')
        return get_response(request)
    return middleware