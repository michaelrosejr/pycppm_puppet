#!/usr/bin/env python3
from dotenv import dotenv_values
from core import clearpass
from core import puppet
from pprint import pprint

# Load access tokens, urls, etc from environment variable
config = dotenv_values(".env")

# Add an endpoint from Puppet
def addEndpoint():
    # Pull data from Puppet. Currently not passing any aruguments, which it
    # should allow.
    # TODO add argumemts to pass
    # puppetData=puppet.getPuppetDataFromFile()
    puppetData = puppet.getPuppetDataFromURL(config['puppet_url'])[0]
    # print(type(puppetData[0]))

    # Create endpoint
    new_endpoint = {
        "mac_address": puppetData["value"]["mac"],
        "description": "Test insert from API",
        "status": "Unknown",
        "attributes": {
            "source": "Puppet script",
            "fqdn": puppetData["value"]["fqdn"],
            "environment": puppetData["environment"],
            "name": puppetData["name"],
            "eth0": puppetData["value"]["interfaces"]["eth0"],
        },
    }

    resp = clearpass.createEndpoint(
        config["cppm_url"], config["cppm_access_token"], new_endpoint
    )

    pprint(resp, indent=4)


if __name__ == "__main__":
    addEndpoint()
