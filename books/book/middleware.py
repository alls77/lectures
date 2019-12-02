def simple_middleware(get_response):
    def middleware(request):
        request.session['test'] = 42

        response = get_response(request)

        return response
    return middleware


class SimpleMidleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response