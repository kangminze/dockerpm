# _*_ coding: utf-8 _*_
from dockerpm.apps.common.docker_client import docker_client


class ContainersService(object):

    def containers(self):
        result = list()
        containers = docker_client().containers.list(all=True)
        if not containers:
            return result
        for container in containers:
            tmp = dict()
            tmp["id"] = container.id
            tmp["name"] = container.name
            tmp["short_id"] = container.short_id
            tmp["status"] = container.status
            tmp["image"] = container.image
            result.append(tmp)
        return result

