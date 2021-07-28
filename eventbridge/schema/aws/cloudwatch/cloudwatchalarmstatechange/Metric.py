# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.Dimensions import Dimensions  # noqa: F401,E501

class Metric(object):


    _types = {
        'dimensions': 'Dimensions',
        'namespace': 'str',
        'name': 'str'
    }

    _attribute_map = {
        'dimensions': 'dimensions',
        'namespace': 'namespace',
        'name': 'name'
    }

    def __init__(self, dimensions=None, namespace=None, name=None):  # noqa: E501
        self._dimensions = None
        self._namespace = None
        self._name = None
        self.discriminator = None
        self.dimensions = dimensions
        self.namespace = namespace
        self.name = name


    @property
    def dimensions(self):

        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):


        self._dimensions = dimensions


    @property
    def namespace(self):

        return self._namespace

    @namespace.setter
    def namespace(self, namespace):


        self._namespace = namespace


    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, name):


        self._name = name

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Metric, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

