from django.conf.urls import url
from views import ContainersViewSet

test = ContainersViewSet.as_view(
    {'get': 'test'}
)

containers = ContainersViewSet.as_view(
    {'get': 'containers'}
)

urlpatterns = [
    url('^test$', test, name="test"),
    url('^json$', containers, name="containers"),
]
