#!/usr/bin/python
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""
Sample script to dump out the initiator connector dictionary on the
current system.

"""
import pprint
import sys

from oslo_config import cfg
from oslo_log import log

from diediedie import auth_args
from diediedie import utils
from os_brick.initiator import connector
from os_brick import initiator

parser = auth_args.parser

CONF = cfg.CONF
log.register_options(CONF)
CONF([], project='brick', version='1.0')
log.setup(CONF, 'brick')
LOG = log.getLogger(__name__)


def main():
    """The main."""
    args = parser.parse_args()
    #initiator = utils.get_initiator()
    #utils.print_dict(initiator, value_align='l', disable_unicode=True)

    # now get iSCSI and FC and list
    root_helper = 'sudo',
    iscsi_c = connector.InitiatorConnector.factory(initiator.ISCSI,
                                                   root_helper)
    paths = iscsi_c.get_all_available_volumes()
    if paths:
        print("iSCSI Devices")
        utils.print_dict(paths, value_align='l', disable_unicode=True)

    fc_c = connector.InitiatorConnector.factory(initiator.FIBRE_CHANNEL,
                                                root_helper)
    paths = fc_c.get_all_available_volumes()
    if paths:
        print("Fibre Channel Devices")
        utils.print_dict(paths, value_align='l', disable_unicode=True)

if __name__ == "__main__":
    main()
