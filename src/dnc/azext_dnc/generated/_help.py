# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['dnc controller'] = """
    type: group
    short-summary: Manage controller with dnc
"""

helps['dnc controller create'] = """
    type: command
    short-summary: "Create a dnc controller."
    examples:
      - name: Create controller
        text: |-
               az dnc controller create --location "West US" --resource-group "TestRG" --resource-name \
"testcontroller"
"""

helps['dnc controller delete'] = """
    type: command
    short-summary: "Deletes the DNC controller."
    examples:
      - name: Delete controller
        text: |-
               az dnc controller delete --resource-group "TestRG" --resource-name "testcontroller"
"""

helps['dnc controller patch'] = """
    type: command
    short-summary: "Update dnc controller."
    examples:
      - name: update controller
        text: |-
               az dnc controller patch --tags key="value" --resource-group "TestRG" --resource-name "testcontroller"
"""

helps['dnc controller show-detail'] = """
    type: command
    short-summary: "Gets details about the specified dnc controller."
    examples:
      - name: Get details of a controller
        text: |-
               az dnc controller show-detail --resource-group "TestRG" --resource-name "testcontroller"
"""

helps['dnc delegated-network'] = """
    type: group
    short-summary: Manage delegated network with dnc
"""

helps['dnc delegated-network list'] = """
    type: command
    short-summary: "Get all the delegatedController resources in a resource group. And Get all the delegatedController \
resources in a subscription."
    examples:
      - name: Get DelegatedNetwork resources by resource group
        text: |-
               az dnc delegated-network list --resource-group "testRG"
      - name: Get DelegatedController resources by subscription
        text: |-
               az dnc delegated-network list
"""

helps['dnc orchestrator-instance-service'] = """
    type: group
    short-summary: Manage orchestrator instance service with dnc
"""

helps['dnc orchestrator-instance-service list'] = """
    type: command
    short-summary: "Get all the OrchestratorInstances resources in a resource group. And Get all the \
orchestratorInstance resources in a subscription."
    examples:
      - name: Get OrchestratorInstance resources by resource group
        text: |-
               az dnc orchestrator-instance-service list --resource-group "testRG"
      - name: Get orchestratorInstance resources by subscription
        text: |-
               az dnc orchestrator-instance-service list
"""

helps['dnc orchestrator-instance-service create'] = """
    type: command
    short-summary: "Create a orchestrator instance."
    examples:
      - name: Create orchestrator instance
        text: |-
               az dnc orchestrator-instance-service create --type "SystemAssigned" --location "West US" \
--api-server-endpoint "https://testk8s.cloudapp.net" --cluster-root-ca "ddsadsad344mfdsfdl" --id \
"/subscriptions/613192d7-503f-477a-9cfe-4efc3ee2bd60/resourceGroups/TestRG/providers/Microsoft.DelegatedNetwork/control\
ler/testcontroller" --orchestrator-app-id "546192d7-503f-477a-9cfe-4efc3ee2b6e1" --orchestrator-tenant-id \
"da6192d7-503f-477a-9cfe-4efc3ee2b6c3" --private-link-resource-id "/subscriptions/613192d7-503f-477a-9cfe-4efc3ee2bd60/\
resourceGroups/TestRG/providers/Microsoft.Network/privateLinkServices/plresource1" --resource-group "TestRG" \
--resource-name "testk8s1"
"""

helps['dnc orchestrator-instance-service delete'] = """
    type: command
    short-summary: "Deletes the Orchestrator Instance."
    examples:
      - name: Delete Orchestrator Instance
        text: |-
               az dnc orchestrator-instance-service delete --resource-group "TestRG" --resource-name "k8stest1"
"""

helps['dnc orchestrator-instance-service patch'] = """
    type: command
    short-summary: "Update Orchestrator Instance."
    examples:
      - name: update Orchestrator Instance
        text: |-
               az dnc orchestrator-instance-service patch --tags key="value" --resource-group "TestRG" --resource-name \
"testk8s1"
"""

helps['dnc orchestrator-instance-service show-detail'] = """
    type: command
    short-summary: "Gets details about the orchestrator instance."
    examples:
      - name: Get details of a orchestratorInstance
        text: |-
               az dnc orchestrator-instance-service show-detail --resource-group "TestRG" --resource-name "testk8s1"
"""

helps['dnc delegated-subnet-service'] = """
    type: group
    short-summary: Manage delegated subnet service with dnc
"""

helps['dnc delegated-subnet-service list'] = """
    type: command
    short-summary: "Get all the DelegatedSubnets resources in a resource group. And Get all the DelegatedSubnets \
resources in a subscription."
    examples:
      - name: Get DelegatedSubnets resources by resource group
        text: |-
               az dnc delegated-subnet-service list --resource-group "testRG"
      - name: Get DelegatedSubnets resources by subscription
        text: |-
               az dnc delegated-subnet-service list
"""

helps['dnc delegated-subnet-service delete'] = """
    type: command
    short-summary: "Delete dnc DelegatedSubnet."
    examples:
      - name: delete delegated subnet
        text: |-
               az dnc delegated-subnet-service delete --resource-group "TestRG" --resource-name "delegated1"
"""

helps['dnc delegated-subnet-service patch-detail'] = """
    type: command
    short-summary: "Patch delegated subnet resource."
    examples:
      - name: patch delegated subnet
        text: |-
               az dnc delegated-subnet-service patch-detail --tags key="value" --resource-group "TestRG" \
--resource-name "delegated1"
"""

helps['dnc delegated-subnet-service put-detail'] = """
    type: command
    short-summary: "Put delegated subnet resource."
    examples:
      - name: put delegated subnet
        text: |-
               az dnc delegated-subnet-service put-detail --location "West US" --id "/subscriptions/613192d7-503f-477a-\
9cfe-4efc3ee2bd60/resourceGroups/TestRG/providers/Microsoft.DelegatedNetwork/controller/dnctestcontroller" \
--subnet-details-id "/subscriptions/613192d7-503f-477a-9cfe-4efc3ee2bd60/resourceGroups/TestRG/providers/Microsoft.Netw\
ork/virtualNetworks/testvnet/subnets/testsubnet" --resource-group "TestRG" --resource-name "delegated1"
"""

helps['dnc delegated-subnet-service show-detail'] = """
    type: command
    short-summary: "Gets details about the specified dnc DelegatedSubnet Link."
    examples:
      - name: Get details of a delegated subnet
        text: |-
               az dnc delegated-subnet-service show-detail --resource-group "TestRG" --resource-name "delegated1"
"""
