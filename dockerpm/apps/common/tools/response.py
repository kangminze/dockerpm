# _*_ coding: utf-8 _*_
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from dockerpm.apps.common.constant import constant_base


def response():
    """
    :param code:
    :return:
    """

    def func_wrapper(func):
        def return_wrapper(*args, **wkargs):
            try:
                success = False
                result = None
                info = None
                level = None

                result = func(*args, **wkargs)
                info = "操作成功"
                level = constant_base.RETURN_LEVEL_INFO
                success = True
            except Http404, e:
                level = constant_base.RETURN_LEVEL_ERROR
                info = "操作失败"
            except IntegrityError, e:
                level = constant_base.RETURN_LEVEL_ERROR
                info = "操作失败"
            except ObjectDoesNotExist, e:
                level = constant_base.RETURN_LEVEL_ERROR
                info = "操作失败"
            except Exception, e:
                level = constant_base.RETURN_LEVEL_ERROR
                info = "操作失败"
            finally:
                result = get_result(success=success, data=result, info=info, level=level)
            return Response(result, status=status.HTTP_200_OK)

        return return_wrapper

    return func_wrapper


class ResultDict(dict):
    """
    前端返回对象
    """

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __call__(self, key):
        return self[key]

    def __init__(self, success=True, data=None, info=None, level=None):
        self.success = success
        self.data = data
        self.info = info
        self.level = level

def get_result(success=True, data=None, info=None, level=None):
    return ResultDict(success, data=data, info=info, level=level)