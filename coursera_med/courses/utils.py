def is_mobile(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    return 'mobi' in user_agent 