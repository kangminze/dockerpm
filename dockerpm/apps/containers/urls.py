from django.conf.urls import url
from views import ContainersViewSet

test = ContainersViewSet.as_view(
    {'get':'test'}
)

urlpatterns = [
    url('^test$', test, name="test")
]