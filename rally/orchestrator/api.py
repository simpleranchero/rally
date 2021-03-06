# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013: Mirantis Inc.
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


from rally.benchmark import engine
from rally import deploy


def start_task(config):
    """Start Benchmark task.
        1) Deploy OpenStack Cloud
        2) Verify Deployment
        3) Run Benchmarks
        4) Process benchmark results
        5) Destroy cloud and cleanup
    Returns task uuid
    """
    deploy_conf = config['deploy']
    deployer = deploy.EngineFactory.get_engine(deploy_conf['name'],
                                               deploy_conf)
    tester = engine.TestEngine(config['tests'])

    with deployer as deployment:
        with tester.bind(deployment):
            tester.verify()
            tester.benchmark()


def abort_task(task_uuid):
    """Abort running task."""
    raise NotImplementedError()
