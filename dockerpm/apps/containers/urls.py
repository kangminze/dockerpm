from django.conf.urls import url
from views import ContainersViewSet

test = ContainersViewSet.as_view(
    {'get': 'test'}
)

containers = ContainersViewSet.as_view(
    {'get': 'containers'}
)

containers_start = ContainersViewSet.as_view(
    {'post': 'start'}
)

urlpatterns = [
    url('^test$', test, name="test"),
    url('^json$', containers, name="containers"),
    url('^start$', containers_start, name="containers_start"),
]
