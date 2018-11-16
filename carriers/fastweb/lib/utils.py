"""
Utility library
"""


def get_client_ip(request):
    """
    Function to return user ip address
    :param request:
    :return: ip address user
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip