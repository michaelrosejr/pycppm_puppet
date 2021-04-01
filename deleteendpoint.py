#!/usr/bin/env python3
from dotenv import dotenv_values
from core import clearpass
from core import puppet
from pprint import pprint

# Load access tokens, urls, etc from environment variable
config = dotenv_values("../xilinux.env")


# Add an endpoint from Puppet
def deleteEndpoint():
    puppetData = puppet.getPuppetDataFromURL(config['puppet_url'])[0]

    resp = clearpass.deleteEndpoint(
        config["cppm_url"], config["cppm_access_token"], puppetData["value"]["mac"]
    )

    return resp


if __name__ == "__main__":
    deleteEndpoint()
