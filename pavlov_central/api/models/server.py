# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from pavlov_central.api.models.base_model_ import Model
from pavlov_central.api import util


class Server(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, ip=None):  # noqa: E501
        """Server - a model defined in OpenAPI

        :param name: The name of this Server.  # noqa: E501
        :type name: str
        :param ip: The ip of this Server.  # noqa: E501
        :type ip: str
        """
        self.openapi_types = {
            'name': str,
            'ip': str
        }

        self.attribute_map = {
            'name': 'name',
            'ip': 'ip'
        }

        self._name = name
        self._ip = ip

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Server of this Server.  # noqa: E501
        :rtype: Server
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Server.


        :return: The name of this Server.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Server.


        :param name: The name of this Server.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this Server.


        :return: The ip of this Server.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Server.


        :param ip: The ip of this Server.
        :type ip: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip
