from django.db.models import QuerySet, Prefetch
from django_filters import filterset

from core import models

FILTER_EQUALS = 'exact'
FILTER_LIKE = 'unaccent__icontains'
FILTER_ISNULL = 'isnull'
FILTER_IN = 'in'


class DepartmentFilter(filterset.FilterSet):
    user_not_in = filterset.NumberFilter(method='filter_user_not_in')

    def filter_user_not_in(self, queryset: QuerySet, name, value):
        return queryset.prefetch_related(
            Prefetch('users', queryset=models.User.objects.exclude(pk=value))
        )

    class Meta:
        model = models.Department
        fields = ['user_not_in']


class UserFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=FILTER_EQUALS)

    class Meta:
        model = models.User
        fields = ['name']
