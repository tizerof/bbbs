from typing import List

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


def has_roles(role_list: List):
    def decor(func):
        def wrapper(*args, **kwagrs):
            current_user_id = args[1].user.id
            current_user_roles = User.objects.filter(id=current_user_id).select_related('extenduser').values(
                'extenduser__roles'
            )
            l = [i['extenduser__roles'] for i in current_user_roles]
            if list(set(role_list) & set(l)):
                r = func(*args, **kwagrs)
                return r
            else:
                return Response(data='Not found', status=status.HTTP_404_NOT_FOUND)
        return wrapper
    return decor
