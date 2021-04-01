import requests
import json


def getEndpoints(baseurl, access_token):
    """Grab a list of all endpoints from ClearPass Endpoints

    Args:
        baseurl ([str]): The URL for ClearPass Policy Manager
        access_token ([str]): The access token for ClearPass Policy Manager
    """
    url = baseurl + "/api/endpoint"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }
    response = requests.get(url, headers=headers, data=payload)

    return(response.text)


def createEndpoint(baseurl, access_token, endpoint):
    """Create an endpoint from ClearPass Endpoints

    Args:
        baseurl ([str]): The URL for ClearPass Policy Manager
        access_token ([str]): The access token for ClearPass Policy Manager
        endpoint ([dict]): A dict of values to be passed to ClearPass Policy Manager
    """
    url = baseurl + "/api/endpoint"

    payload = json.dumps(endpoint)
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json',
    }

    response = requests.post(url, headers=headers, data=payload)

    return(response.text)

def deleteEndpoint(baseurl, access_token, mac_address):
    """Deletes an endpoint from ClearPass Policy Manager

    Args:
        baseurl ([str]): The URL for ClearPass Policy Manager
        access_token ([str]): The access token for ClearPass Policy Manager
        mac_address ([str]): MAC address of client that you wish to be deleted from ClearPass
    """
    url = baseurl + "/api/endpoint/mac-address/" + mac_address

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json',
    }

    response = requests.delete(url, headers=headers)

    return(response.text)  