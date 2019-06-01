from rest_framework.exceptions import APIException
from django.utils.translation import ugettext_lazy as _


class UserCanNotBeSomeException(APIException):
    status_code = 400
    default_detail = _('Users can not be some')
