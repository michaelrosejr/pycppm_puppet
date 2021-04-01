import requests
import json


def getPuppetDataFromFile():
    """Used to test script. Uses test data from puppet and stores it 
    in a file.

    Returns:
        [type]: [description]
    """
    with open("puppet_resp.json", "r") as f:
        puppetdata = json.load(f)

    return puppetdata


def getPuppetDataFromURL(url):
    """Pulls data from Puppet to be used to create a new endpoint in ClearPass

    Args:
        url ([string]): Url of Puppet server

    Returns:
        [list]: Returns a list of dicts of facts stored in Puppet
    """
    headers = {
        # They key below is used for development. It can be removed.
        "x-api-key": "PMAK-6063951bfb834d0052b53dca-339f7852e06ed1434a4e8c7cca3ad7d9e4"
    }

    resp = requests.get(url, headers=headers)

    return resp.json()


if __name__ == "__main__":
    getPuppetDataFromURL()
