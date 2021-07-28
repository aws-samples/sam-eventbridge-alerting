# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.CloudWatchAlarmStateChange import CloudWatchAlarmStateChange  # noqa: F401,E501

class AWSEvent(object):


    _types = {
        'detail': 'CloudWatchAlarmStateChange',
        'detail_type': 'str',
        'resources': 'list[str]',
        'id': 'str',
        'source': 'str',
        'time': 'datetime',
        'region': 'str',
        'version': 'str',
        'account': 'str'
    }

    _attribute_map = {
        'detail': 'detail',
        'detail_type': 'detail-type',
        'resources': 'resources',
        'id': 'id',
        'source': 'source',
        'time': 'time',
        'region': 'region',
        'version': 'version',
        'account': 'account'
    }

    def __init__(self, detail=None, detail_type=None, resources=None, id=None, source=None, time=None, region=None, version=None, account=None):  # noqa: E501
        self._detail = None
        self._detail_type = None
        self._resources = None
        self._id = None
        self._source = None
        self._time = None
        self._region = None
        self._version = None
        self._account = None
        self.discriminator = None
        self.detail = detail
        self.detail_type = detail_type
        self.resources = resources
        self.id = id
        self.source = source
        self.time = time
        self.region = region
        self.version = version
        self.account = account


    @property
    def detail(self):

        return self._detail

    @detail.setter
    def detail(self, detail):


        self._detail = detail


    @property
    def detail_type(self):

        return self._detail_type

    @detail_type.setter
    def detail_type(self, detail_type):


        self._detail_type = detail_type


    @property
    def resources(self):

        return self._resources

    @resources.setter
    def resources(self, resources):


        self._resources = resources


    @property
    def id(self):

        return self._id

    @id.setter
    def id(self, id):


        self._id = id


    @property
    def source(self):

        return self._source

    @source.setter
    def source(self, source):


        self._source = source


    @property
    def time(self):

        return self._time

    @time.setter
    def time(self, time):


        self._time = time


    @property
    def region(self):

        return self._region

    @region.setter
    def region(self, region):


        self._region = region


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version


    @property
    def account(self):

        return self._account

    @account.setter
    def account(self, account):


        self._account = account

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
        if issubclass(AWSEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AWSEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

