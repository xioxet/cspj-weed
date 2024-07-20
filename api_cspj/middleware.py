from django.http import HttpResponseForbidden

def restrict_access_middleware(get_response, *args, **kwargs):
    def middleware(request, *args, **kwargs):
        if request.META.get('REMOTE_ADDR') != '127.0.0.1':
            print(request.META)
            return HttpResponseForbidden(f'Access Denied')
        return get_response(request, *args, **kwargs)
    return middleware