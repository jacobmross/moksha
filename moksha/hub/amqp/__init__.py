# This file is part of Moksha.
# Copyright (C) 2008-2010  Red Hat, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Here is where we configure which AMQP hub implementation we are going to use.
"""
import logging
log = logging.getLogger(__name__)

try:
    from qpid010 import QpidAMQPHub
    AMQPHub = QpidAMQPHub
except ImportError:
    log.debug("Cannot find qpid python module")
    try:
        from pyamqplib import AMQPLibHub
        AMQPHub = AMQPLibHub
    except ImportError:
        log.debug("Cannot find pyamqplib")
        log.debug("Using FakeHub AMQP broker. Don't expect AMQP to work")
        class FakeHub(object):
            pass
        AMQPHub = FakeHub

