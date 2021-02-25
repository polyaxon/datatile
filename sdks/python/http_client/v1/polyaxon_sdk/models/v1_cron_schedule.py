#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1CronSchedule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'kind': 'str',
        'start_at': 'datetime',
        'end_at': 'datetime',
        'max_runs': 'int',
        'cron': 'str',
        'depends_on_past': 'bool'
    }

    attribute_map = {
        'kind': 'kind',
        'start_at': 'startAt',
        'end_at': 'endAt',
        'max_runs': 'maxRuns',
        'cron': 'cron',
        'depends_on_past': 'dependsOnPast'
    }

    def __init__(self, kind='cron', start_at=None, end_at=None, max_runs=None, cron=None, depends_on_past=None, local_vars_configuration=None):  # noqa: E501
        """V1CronSchedule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._start_at = None
        self._end_at = None
        self._max_runs = None
        self._cron = None
        self._depends_on_past = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if max_runs is not None:
            self.max_runs = max_runs
        if cron is not None:
            self.cron = cron
        if depends_on_past is not None:
            self.depends_on_past = depends_on_past

    @property
    def kind(self):
        """Gets the kind of this V1CronSchedule.  # noqa: E501


        :return: The kind of this V1CronSchedule.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1CronSchedule.


        :param kind: The kind of this V1CronSchedule.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def start_at(self):
        """Gets the start_at of this V1CronSchedule.  # noqa: E501


        :return: The start_at of this V1CronSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this V1CronSchedule.


        :param start_at: The start_at of this V1CronSchedule.  # noqa: E501
        :type: datetime
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this V1CronSchedule.  # noqa: E501


        :return: The end_at of this V1CronSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this V1CronSchedule.


        :param end_at: The end_at of this V1CronSchedule.  # noqa: E501
        :type: datetime
        """

        self._end_at = end_at

    @property
    def max_runs(self):
        """Gets the max_runs of this V1CronSchedule.  # noqa: E501


        :return: The max_runs of this V1CronSchedule.  # noqa: E501
        :rtype: int
        """
        return self._max_runs

    @max_runs.setter
    def max_runs(self, max_runs):
        """Sets the max_runs of this V1CronSchedule.


        :param max_runs: The max_runs of this V1CronSchedule.  # noqa: E501
        :type: int
        """

        self._max_runs = max_runs

    @property
    def cron(self):
        """Gets the cron of this V1CronSchedule.  # noqa: E501


        :return: The cron of this V1CronSchedule.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this V1CronSchedule.


        :param cron: The cron of this V1CronSchedule.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def depends_on_past(self):
        """Gets the depends_on_past of this V1CronSchedule.  # noqa: E501


        :return: The depends_on_past of this V1CronSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._depends_on_past

    @depends_on_past.setter
    def depends_on_past(self, depends_on_past):
        """Sets the depends_on_past of this V1CronSchedule.


        :param depends_on_past: The depends_on_past of this V1CronSchedule.  # noqa: E501
        :type: bool
        """

        self._depends_on_past = depends_on_past

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CronSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CronSchedule):
            return True

        return self.to_dict() != other.to_dict()
