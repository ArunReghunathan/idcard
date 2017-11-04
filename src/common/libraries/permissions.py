from django.http import JsonResponse
from rest_framework import status
from src.common.constants.project_constants import PERMISSION_DENIED


def check_permissions(permissionsLevel):
    def arg(function):
        def wrap(request, *args, **kwargs):
            if request.userinfo.premissiom_level >= permissionsLevel:
                result = function(request, *args, **kwargs)
                return result
            else:
                return JsonResponse(PERMISSION_DENIED, status=status.HTTP_401_UNAUTHORIZED)
        return wrap
    return arg

def cls_check_permissions(permissionsLevel):
    def arg(function):
        def wrap(request, *args, **kwargs):
            if args[0].userinfo.premissiom_level >= permissionsLevel:
                result = function(request, *args, **kwargs)
                return result
            else:
                return JsonResponse(PERMISSION_DENIED, status=status.HTTP_401_UNAUTHORIZED)
        return wrap
    return arg