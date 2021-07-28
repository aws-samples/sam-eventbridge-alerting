# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.cloudwatch.cloudwatchalarmstatechange.Configuration import Configuration  # noqa: F401,E501
from schema.aws.cloudwatch.cloudwatchalarmstatechange.State import State  # noqa: F401,E501

class CloudWatchAlarmStateChange(object):


    _types = {
        'configuration': 'Configuration',
        'state': 'State',
        'previousState': 'State',
        'alarmName': 'str'
    }

    _attribute_map = {
        'configuration': 'configuration',
        'state': 'state',
        'previousState': 'previousState',
        'alarmName': 'alarmName'
    }

    def __init__(self, configuration=None, state=None, previousState=None, alarmName=None):  # noqa: E501
        self._configuration = None
        self._state = None
        self._previousState = None
        self._alarmName = None
        self.discriminator = None
        self.configuration = configuration
        self.state = state
        self.previousState = previousState
        self.alarmName = alarmName


    @property
    def configuration(self):

        return self._configuration

    @configuration.setter
    def configuration(self, configuration):


        self._configuration = configuration


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state


    @property
    def previousState(self):

        return self._previousState

    @previousState.setter
    def previousState(self, previousState):


        self._previousState = previousState


    @property
    def alarmName(self):

        return self._alarmName

    @alarmName.setter
    def alarmName(self, alarmName):


        self._alarmName = alarmName

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
        if issubclass(CloudWatchAlarmStateChange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CloudWatchAlarmStateChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

