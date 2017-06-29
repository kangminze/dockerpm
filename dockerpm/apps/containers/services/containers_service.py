# _*_ coding: utf-8 _*_
from dockerpm.apps.common.docker_client import docker_client


class ContainersService(object):

    def containers(self):
        client = docker_client()
        client.containers.list()


ContainersService().containers()
