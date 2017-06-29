# -*- coding: utf-8

from rest_framework import (viewsets, status)
from rest_framework.response import Response


class ContainersViewSet(viewsets.ModelViewSet):

    def test(self, request):
        print "hello world"
        return Response(True, status.HTTP_200_OK)