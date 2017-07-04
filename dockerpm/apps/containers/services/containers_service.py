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
            tmp["id"] = container.id.encode('utf-8')
            tmp["name"] = container.name.encode('utf-8')
            tmp["short_id"] = container.short_id.encode('utf-8')
            tmp["status"] = container.status.encode('utf-8')
            tmp["image"] = container.image.tags[0].encode('utf-8')
            result.append(tmp)
        return result

