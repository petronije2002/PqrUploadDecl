
## AADTokenCredentials for multi-factor authentication
from msrestazure.azure_active_directory import AADTokenCredentials

## Required for Azure Data Lake Analytics job management
from azure.mgmt.datalake.analytics.job import DataLakeAnalyticsJobManagementClient
from azure.mgmt.datalake.analytics.job.models import JobInformation, JobState, USqlJobProperties
from requests.models import PreparedRequest
## Other required imports
import adal, uuid, time
import requests
import urllib.request


import random, threading, webbrowser

def authenticate_device_code():
    """
    Authenticate the end-user using device auth.
    """

    tenant_id = 'c6b55c72-f303-4477-b825-caf9ff7a9f48' 
    client_id = 'cf9c7863-14b9-425f-b660-11214e760fef'


    base_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/'.format(tenant_id) + 'authorize'#.format(client_id)




    params = {"client_id": str(client_id),
            "response_type": "code",
            "redirect_uri=": 'http://localhost:5000/myapp',
            "response_mode": "query" ,
            "scope":"User.Read User.ReadBasic.All",
            "state": "42343"}

    req = PreparedRequest()
    req.prepare_url(base_url, params)

    # import urllib.request
    # with urllib.request.urlopen(req.url) as response:
    #     html = response.read()


    # urllib.request.urlopen(req.url)
    # # response = urllib.urlopen(req.url)
    # # r = requests.post(req.url)

    port = 5000 + random.randint(0, 999)
    url = req.url + ":{0}".format(port)


    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()


    

    return 



# # url_= 'https://login.microsoftonline.com/c6b55c72-f303-4477-b825-caf9ff7a9f48/oauth2/v2.0/authorize?cf9c7863-14b9-425f-b660-11214e760fef&response_type=code&redirect_uri%3D=http%3A%2F%2Flocalhost%2Fmyapp&response_mode=query&scope=User.Read%20User.ReadBasic.All&state=42343'
 
# # url_ = 'https://login.microsoftonline.com/c6b55c72-f303-4477-b825-caf9ff7a9f48/oauth2/v2.0/?authorize=cf9c7863-14b9-425f-b660-11214e760fef&response_type=code&redirect_uri%3D=https%3A%2F%2Flocalhost%2Fmyapp&response_mode=query&scope=User.Read+User.ReadBasic.All&state=42343'
# # #urllib.parse.quote
# authority_uri = authority_host_uri + '/' + tenant_id + client_id

# response_type='code'

# auth_url = "https://login.microsoftonline.com/{}".format(tenant_id) + client_id


#     client_id=6731de76-14a6-49ae-97bc-6eba6914391e
#     &response_type=code
#     &redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2F
#     &response_mode=query
#     &scope=offline_access%20user.read%20mail.read
#     &state=12345




#     # resource_uri = 'https://management.core.windows.net/'

#     resource_uri= 'https://graph.microsoft.com/v1.0/me'
#     client_id = 'cf9c7863-14b9-425f-b660-11214e760fef'

#     context = adal.AuthenticationContext(authority_uri, api_version=None)
#     code = context.acquire_user_code(resource_uri, client_id)
#     print(code['message'])
#     mgmt_token = context.acquire_token_with_device_code(resource_uri, code, client_id)
#     credentials = AADTokenCredentials(mgmt_token, client_id)

#     return credentials

