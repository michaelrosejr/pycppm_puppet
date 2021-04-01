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

    }

    resp = requests.get(url, headers=headers)

    return resp.json()


if __name__ == "__main__":
    getPuppetDataFromURL()
