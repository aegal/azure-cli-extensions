# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ControllerDetails(msrest.serialization.Model):
    """controller details.

    :param id: controller arm resource id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ControllerDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class ControllerResource(msrest.serialization.Model):
    """Represents an instance of a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ControllerResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class ControllerResourceUpdateParameters(msrest.serialization.Model):
    """Parameters for updating a resource.

    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ControllerResourceUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class DelegatedController(ControllerResource):
    """Represents an instance of a DNC controller.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    :ivar properties: Properties of the provision operation request.
    :vartype properties: ~dnc.models.DelegatedControllerProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'DelegatedControllerProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedController, self).__init__(**kwargs)
        self.properties = None


class DelegatedControllerProperties(msrest.serialization.Model):
    """Properties of Delegated controller resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar resource_guid: Resource guid.
    :vartype resource_guid: str
    :ivar provisioning_state: The current state of dnc controller resource. Possible values
     include: "Deleting", "Succeeded", "Failed", "Provisioning".
    :vartype provisioning_state: str or ~dnc.models.ControllerState
    :ivar dnc_app_id: dnc application id should be used by customer to authenticate with dnc
     gateway.
    :vartype dnc_app_id: str
    :ivar dnc_tenant_id: tenant id of dnc application id.
    :vartype dnc_tenant_id: str
    :ivar dnc_endpoint: dnc endpoint url that customers can use to connect to.
    :vartype dnc_endpoint: str
    """

    _validation = {
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'dnc_app_id': {'readonly': True},
        'dnc_tenant_id': {'readonly': True},
        'dnc_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'resource_guid': {'key': 'resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'dnc_app_id': {'key': 'dncAppId', 'type': 'str'},
        'dnc_tenant_id': {'key': 'dncTenantId', 'type': 'str'},
        'dnc_endpoint': {'key': 'dncEndpoint', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedControllerProperties, self).__init__(**kwargs)
        self.resource_guid = None
        self.provisioning_state = None
        self.dnc_app_id = None
        self.dnc_tenant_id = None
        self.dnc_endpoint = None


class DelegatedControllers(msrest.serialization.Model):
    """An array of Delegated controller resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. An array of Delegated controller resources.
    :type value: list[~dnc.models.DelegatedController]
    :ivar next_link: The URL to get the next set of controllers.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DelegatedController]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedControllers, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class DelegatedSubnetResource(msrest.serialization.Model):
    """Represents an instance of a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedSubnetResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class DelegatedSubnet(DelegatedSubnetResource):
    """Represents an instance of a orchestrator.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    :ivar resource_guid: Resource guid.
    :vartype resource_guid: str
    :ivar provisioning_state: The current state of dnc delegated subnet resource. Possible values
     include: "Deleting", "Succeeded", "Failed", "Provisioning".
    :vartype provisioning_state: str or ~dnc.models.DelegatedSubnetState
    :param subnet_details: subnet details.
    :type subnet_details: ~dnc.models.SubnetDetails
    :param controller_details: Properties of the controller.
    :type controller_details: ~dnc.models.ControllerDetails
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'subnet_details': {'key': 'properties.subnetDetails', 'type': 'SubnetDetails'},
        'controller_details': {'key': 'properties.controllerDetails', 'type': 'ControllerDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedSubnet, self).__init__(**kwargs)
        self.resource_guid = None
        self.provisioning_state = None
        self.subnet_details = kwargs.get('subnet_details', None)
        self.controller_details = kwargs.get('controller_details', None)


class DelegatedSubnets(msrest.serialization.Model):
    """An array of DelegatedSubnet resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. An array of DelegatedSubnet resources.
    :type value: list[~dnc.models.DelegatedSubnet]
    :ivar next_link: The URL to get the next set of DelegatedSubnet resources.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DelegatedSubnet]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DelegatedSubnets, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~dnc.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~dnc.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~dnc.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Operation(msrest.serialization.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for data-
     plane operations and "false" for ARM/control-plane operations.
    :vartype is_data_action: bool
    :param display: Localized display information for this particular operation.
    :type display: ~dnc.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Possible values include: "user",
     "system", "user,system".
    :vartype origin: str or ~dnc.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. Possible values include: "Internal".
    :vartype action_type: str or ~dnc.models.ActionType
    """

    _validation = {
        'name': {'readonly': True},
        'is_data_action': {'readonly': True},
        'origin': {'readonly': True},
        'action_type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'action_type': {'key': 'actionType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = kwargs.get('display', None)
        self.origin = None
        self.action_type = None


class OperationDisplay(msrest.serialization.Model):
    """Localized display information for this particular operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(msrest.serialization.Model):
    """A list of REST API operations supported by an Azure Resource Provider. It contains an URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~dnc.models.Operation]
    :ivar next_link: URL to get the next set of operation list results (if there are any).
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class OrchestratorResource(msrest.serialization.Model):
    """Represents an instance of a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param kind: Required. The kind of workbook. Choices are user and shared. Possible values
     include: "Kubernetes".
    :type kind: str or ~dnc.models.OrchestratorKind
    :param identity: The identity of the orchestrator.
    :type identity: ~dnc.models.OrchestratorIdentity
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'OrchestratorIdentity'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.kind = kwargs['kind']
        self.identity = kwargs.get('identity', None)
        self.tags = kwargs.get('tags', None)


class Orchestrator(OrchestratorResource):
    """Represents an instance of a orchestrator.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: An identifier that represents the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of resource.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param kind: Required. The kind of workbook. Choices are user and shared. Possible values
     include: "Kubernetes".
    :type kind: str or ~dnc.models.OrchestratorKind
    :param identity: The identity of the orchestrator.
    :type identity: ~dnc.models.OrchestratorIdentity
    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    :param properties: Properties of the provision operation request.
    :type properties: ~dnc.models.OrchestratorResourceProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'OrchestratorIdentity'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'OrchestratorResourceProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Orchestrator, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class OrchestratorIdentity(msrest.serialization.Model):
    """OrchestratorIdentity.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal id of the system assigned identity which is used by
     orchestrator.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id of the system assigned identity which is used by orchestrator.
    :vartype tenant_id: str
    :param type: The type of identity used for orchestrator cluster. Type 'SystemAssigned' will use
     an implicitly created identity orchestrator clusters. Possible values include:
     "SystemAssigned", "None".
    :type type: str or ~dnc.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class OrchestratorResourceProperties(msrest.serialization.Model):
    """Properties of orchestrator.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar resource_guid: Resource guid.
    :vartype resource_guid: str
    :ivar provisioning_state: The current state of orchestratorInstance resource. Possible values
     include: "Deleting", "Succeeded", "Failed", "Provisioning".
    :vartype provisioning_state: str or ~dnc.models.OrchestratorInstanceState
    :param orchestrator_app_id: AAD ID used with apiserver.
    :type orchestrator_app_id: str
    :param orchestrator_tenant_id: TenantID of server App ID.
    :type orchestrator_tenant_id: str
    :param cluster_root_ca: RootCA certificate of kubernetes cluster base64 encoded.
    :type cluster_root_ca: str
    :param api_server_endpoint: K8s APIServer url. Either one of apiServerEndpoint or
     privateLinkResourceId can be specified.
    :type api_server_endpoint: str
    :param private_link_resource_id: private link arm resource id. Either one of apiServerEndpoint
     or privateLinkResourceId can be specified.
    :type private_link_resource_id: str
    :param controller_details: Required. Properties of the controller.
    :type controller_details: ~dnc.models.ControllerDetails
    """

    _validation = {
        'resource_guid': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'controller_details': {'required': True},
    }

    _attribute_map = {
        'resource_guid': {'key': 'resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'orchestrator_app_id': {'key': 'orchestratorAppId', 'type': 'str'},
        'orchestrator_tenant_id': {'key': 'orchestratorTenantId', 'type': 'str'},
        'cluster_root_ca': {'key': 'clusterRootCA', 'type': 'str'},
        'api_server_endpoint': {'key': 'apiServerEndpoint', 'type': 'str'},
        'private_link_resource_id': {'key': 'privateLinkResourceId', 'type': 'str'},
        'controller_details': {'key': 'controllerDetails', 'type': 'ControllerDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorResourceProperties, self).__init__(**kwargs)
        self.resource_guid = None
        self.provisioning_state = None
        self.orchestrator_app_id = kwargs.get('orchestrator_app_id', None)
        self.orchestrator_tenant_id = kwargs.get('orchestrator_tenant_id', None)
        self.cluster_root_ca = kwargs.get('cluster_root_ca', None)
        self.api_server_endpoint = kwargs.get('api_server_endpoint', None)
        self.private_link_resource_id = kwargs.get('private_link_resource_id', None)
        self.controller_details = kwargs['controller_details']


class OrchestratorResourceUpdateParameters(msrest.serialization.Model):
    """Parameters for updating a resource.

    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorResourceUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class Orchestrators(msrest.serialization.Model):
    """An array of OrchestratorInstance resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. An array of OrchestratorInstance resources.
    :type value: list[~dnc.models.Orchestrator]
    :ivar next_link: The URL to get the next set of orchestrators.
    :vartype next_link: str
    """

    _validation = {
        'value': {'required': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Orchestrator]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Orchestrators, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = None


class ResourceUpdateParameters(msrest.serialization.Model):
    """Parameters for updating a resource.

    :param tags: A set of tags. The resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class SubnetDetails(msrest.serialization.Model):
    """Properties of orchestrator.

    :param id: subnet arm resource id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubnetDetails, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
