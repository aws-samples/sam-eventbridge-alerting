# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.Metric import Metric  # noqa: F401,E501

class MetricStat(object):


    _types = {
        'metric': 'Metric',
        'period': 'float',
        'stat': 'str'
    }

    _attribute_map = {
        'metric': 'metric',
        'period': 'period',
        'stat': 'stat'
    }

    def __init__(self, metric=None, period=None, stat=None):  # noqa: E501
        self._metric = None
        self._period = None
        self._stat = None
        self.discriminator = None
        self.metric = metric
        self.period = period
        self.stat = stat


    @property
    def metric(self):

        return self._metric

    @metric.setter
    def metric(self, metric):


        self._metric = metric


    @property
    def period(self):

        return self._period

    @period.setter
    def period(self, period):


        self._period = period


    @property
    def stat(self):

        return self._stat

    @stat.setter
    def stat(self, stat):


        self._stat = stat

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
        if issubclass(MetricStat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, MetricStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

