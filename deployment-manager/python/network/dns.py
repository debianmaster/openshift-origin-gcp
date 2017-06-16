# Copyright 2017 BBVA. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates the managed zone."""


def GenerateConfig(context):

  resources = [{
      'name': context.properties['name'],
      'type': 'dns.v1.managedZone',
      'properties': {
          'dnsName': context.properties['dns_name'],
          'description': context.properties['name'] + ' domain'
      }
  }]

  return {'resources': resources}