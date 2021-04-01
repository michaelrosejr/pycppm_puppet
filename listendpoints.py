#!/usr/bin/env python3
from dotenv import dotenv_values
from core import clearpass
from pprint import pprint

# Load access tokens, urls, etc from environment variable
config = dotenv_values(".env")

# Get a list of all endpoints in the ClearPass Endpoints DB
def getAllEndpoints():
    GetAllEndpoints = clearpass.getEndpoints(
        config['cppm_url'], config['cppm_access_token']
    )
    return GetAllEndpoints


if __name__ == "__main__":
    pprint(getAllEndpoints(), indent=4)