from .utils import is_mobile

def mobile_detector(request):
    return {
        'is_mobile': is_mobile(request)
    }