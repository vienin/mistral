# All Rights Reserved.
#
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
from oslo_policy import policy

from mistral.policies import base

TASKS = 'tasks:%s'

rules = [
    policy.DocumentedRuleDefault(
        name=TASKS % 'get',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Return the specified task.',
        operations=[
            {
                'path': '/v2/tasks/{task_id}',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=TASKS % 'list',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Return all tasks.',
        operations=[
            {
                'path': '/v2/tasks',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=TASKS % 'list:all_projects',
        check_str=base.RULE_ADMIN_ONLY,
        description='Return all tasks from all projects.',
        operations=[
            {
                'path': '/v2/tasks',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name=TASKS % 'update',
        check_str=base.RULE_ADMIN_OR_OWNER,
        description='Update the specified task execution.',
        operations=[
            {
                'path': '/v2/tasks',
                'method': 'PUT'
            }
        ]
    )
]


def list_rules():
    return rules
