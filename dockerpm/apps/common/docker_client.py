# _*_ coding: utf-8 _*_

from docker import DockerClient


def docker_client():
    client = DockerClient(base_url='tcp://172.27.44.124:2375')
    return client
