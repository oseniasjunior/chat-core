from django.db.models import Prefetch

from core import models


class DepartmentViewSetMixin:
    @staticmethod
    def get_queryset_default_or_prefetch(request):
        if 'user_not_in' in request.query_params:
            return models.Department.objects.all()
        return models.Department.objects.prefetch_related(
            Prefetch('users', queryset=models.User.objects.all())
        ).all()
