# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.MetricStat import MetricStat  # noqa: F401,E501

class ConfigurationItem(object):


    _types = {
        'metricStat': 'MetricStat',
        'returnData': 'bool',
        'id': 'str'
    }

    _attribute_map = {
        'metricStat': 'metricStat',
        'returnData': 'returnData',
        'id': 'id'
    }

    def __init__(self, metricStat=None, returnData=None, id=None):  # noqa: E501
        self._metricStat = None
        self._returnData = None
        self._id = None
        self.discriminator = None
        self.metricStat = metricStat
        self.returnData = returnData
        self.id = id


    @property
    def metricStat(self):

        return self._metricStat

    @metricStat.setter
    def metricStat(self, metricStat):


        self._metricStat = metricStat


    @property
    def returnData(self):

        return self._returnData

    @returnData.setter
    def returnData(self, returnData):


        self._returnData = returnData


    @property
    def id(self):

        return self._id

    @id.setter
    def id(self, id):


        self._id = id

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
        if issubclass(ConfigurationItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

