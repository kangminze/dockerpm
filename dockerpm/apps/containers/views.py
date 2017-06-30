# -*- coding: utf-8

from rest_framework import (viewsets, status)
from rest_framework.response import Response
from dockerpm.apps.common.tools.response import response


class ContainersViewSet(viewsets.ModelViewSet):

    def test(self, request):
        print "hello world"
        return Response(True, status.HTTP_200_OK)

    @response()
    def containers(self, request):
        return Response()