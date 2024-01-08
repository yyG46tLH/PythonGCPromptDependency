import PureCloudPlatformClientV2 as mygcp
import os
from GCCLogger import *

def read_sdk_config(mygcp):
    # print('...at read_sdk_config...') for debugging only
    mygcp.configuration.config_file_path = os.environ['GENESYS_CLOUD_SDK_CONFIG_PATH']
    return mygcp


def set_platform(mygcp, myregion):
    # print('...at set_platform...') for debugging only
    # Set environment
    region = mygcp.PureCloudRegionHosts[myregion]
    mygcp.configuration.host = region.get_api_host()
    return mygcp

def get_access_token(mygcp, myregion):
    # print('...at get_access_token...') for debugging only
    mygcp = set_platform(mygcp, myregion)
    mytoken = mygcp.api_client.ApiClient().get_client_credentials_token(
        os.environ['GENESYS_CLOUD_CLIENT_ID'], os.environ['GENESYS_CLOUD_CLIENT_SECRET'])
    # print(apiclient)
    # print(authApi.get_authorization_permissions())
    return mygcp, mytoken


def initialize_my_gcp(mygcp):
    # Credentials
    CLIENT_ID = os.environ['GENESYS_CLOUD_CLIENT_ID']
    CLIENT_SECRET = os.environ['GENESYS_CLOUD_CLIENT_SECRET']
    ORG_REGION = os.environ['GENESYS_CLOUD_REGION']

    # Set Platform
    mygcp = set_platform(mygcp, ORG_REGION)

    # Authenticate
    mygcp, mytoken = get_access_token(mygcp, ORG_REGION)

    # Read SDK config
    mygcp = read_sdk_config(mygcp)

    # Set SDK logging
    mygcp = set_gcp_sdk_logging(mygcp)

    return mygcp, mytoken