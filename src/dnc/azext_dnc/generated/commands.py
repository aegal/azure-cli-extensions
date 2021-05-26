# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_dnc.generated._client_factory import cf_controller
    dnc_controller = CliCommandType(
        operations_tmpl='azext_dnc.vendored_sdks.dnc.operations._controller_operations#ControllerOperations.{}',
        client_factory=cf_controller)
    with self.command_group('dnc controller', dnc_controller, client_factory=cf_controller) as g:
        g.custom_command('create', 'dnc_controller_create')
        g.custom_command('delete', 'dnc_controller_delete', confirmation=True)
        g.custom_command('patch', 'dnc_controller_patch')
        g.custom_command('show-detail', 'dnc_controller_show_detail')

    from azext_dnc.generated._client_factory import cf_delegated_network
    dnc_delegated_network = CliCommandType(
        operations_tmpl='azext_dnc.vendored_sdks.dnc.operations._delegated_network_operations#DelegatedNetworkOperation'
        's.{}',
        client_factory=cf_delegated_network)
    with self.command_group('dnc delegated-network', dnc_delegated_network, client_factory=cf_delegated_network) as g:
        g.custom_command('list', 'dnc_delegated_network_list')

    from azext_dnc.generated._client_factory import cf_orchestrator_instance_service
    dnc_orchestrator_instance_service = CliCommandType(
        operations_tmpl='azext_dnc.vendored_sdks.dnc.operations._orchestrator_instance_service_operations#OrchestratorI'
        'nstanceServiceOperations.{}',
        client_factory=cf_orchestrator_instance_service)
    with self.command_group('dnc orchestrator-instance-service', dnc_orchestrator_instance_service,
                            client_factory=cf_orchestrator_instance_service) as g:
        g.custom_command('list', 'dnc_orchestrator_instance_service_list')
        g.custom_command('create', 'dnc_orchestrator_instance_service_create')
        g.custom_command('delete', 'dnc_orchestrator_instance_service_delete', confirmation=True)
        g.custom_command('patch', 'dnc_orchestrator_instance_service_patch')
        g.custom_command('show-detail', 'dnc_orchestrator_instance_service_show_detail')

    from azext_dnc.generated._client_factory import cf_delegated_subnet_service
    dnc_delegated_subnet_service = CliCommandType(
        operations_tmpl='azext_dnc.vendored_sdks.dnc.operations._delegated_subnet_service_operations#DelegatedSubnetSer'
        'viceOperations.{}',
        client_factory=cf_delegated_subnet_service)
    with self.command_group('dnc delegated-subnet-service', dnc_delegated_subnet_service,
                            client_factory=cf_delegated_subnet_service) as g:
        g.custom_command('list', 'dnc_delegated_subnet_service_list')
        g.custom_command('delete', 'dnc_delegated_subnet_service_delete', confirmation=True)
        g.custom_command('patch-detail', 'dnc_delegated_subnet_service_patch_detail')
        g.custom_command('put-detail', 'dnc_delegated_subnet_service_put_detail')
        g.custom_command('show-detail', 'dnc_delegated_subnet_service_show_detail')

    with self.command_group('dnc', is_experimental=True):
        pass
