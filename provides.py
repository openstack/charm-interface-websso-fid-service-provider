# Copyright 2017 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from charms.reactive import hook
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class WebSSOFIDServiceProviderProvides(Endpoint):
    def publish(self, protocol_name, idp_name, user_facing_name):
        # can have multiple dashboard charms in general, therefore,
        # all relation objects and all units must be handled
        # to_publish/relation_set work on a per-relation basis
       for rel in self.relations:
           rel.to_publish['protocol-name'] = protocol_name
           rel.to_publish['idp-name'] = idp_name
           rel.to_publish['user-facing-name'] = user_facing_name
