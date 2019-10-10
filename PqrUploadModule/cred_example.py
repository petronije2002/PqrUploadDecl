mport datetime
import logging
import os
import pandas as pd
import pyodbc 
import urllib.request 
from sqlalchemy import create_engine
import pyodbc
from azure.common.client_factory import get_client_from_json_dict

from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.containerinstance.operations import  ContainerGroupsOperations

import azure.functions as func

from azure.keyvault import KeyVaultClient
from azure.common.credentials import ServicePrincipalCredentials


# Now we need to take credentials for AzureSQL

ContainerTriggerID = os.environ.get("ContainerTriggerID")
ContainerTriggerSecret = os.environ.get("ContainerTriggerSecret")
TenatID = os.environ.get("TenatID")
subscription_id = os.environ.get("subscription_id")

# ContainerTriggerID ="e59998de-9779-4970-97e4-6ad1e4f3e222"
# ContainerTriggerSecret="[O+EmCX.kfA*86EQ9Vm0gnZHorYHWk+-"
# TenatID="c6b55c72-f303-4477-b825-caf9ff7a9f48"
# subscription_id = "d7976a7b-c125-4546-805f-0882eeb271e5"

# VAULT_URL = os.environ.get("VAULT_URL")


credentials = ServicePrincipalCredentials(
    client_id = ContainerTriggerID,
    secret = ContainerTriggerSecret,
    tenant = TenatID
)

api_client = ContainerInstanceManagementClient(credentials,subscription_id)
