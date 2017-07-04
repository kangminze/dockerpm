# -*- coding: utf-8

from rest_framework import (viewsets, status)
from rest_framework.response import Response
from dockerpm.apps.common.tools.response import response
from dockerpm.apps.containers.services.containers_service import ContainersService


class ContainersViewSet(viewsets.ModelViewSet):


    containerService = ContainersService()


    def test(self, request):
        print "hello world"
        return Response(True, status.HTTP_200_OK)

    @response()
    def containers(self, request):
        result = self.containerService.containers()
        return result

    def start(self, request):
        pass