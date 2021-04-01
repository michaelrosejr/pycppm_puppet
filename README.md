# pycppm_puppet 

These scripts will pull facts from Puppet's networking API and create an endpoint in ClearPass.
At this time, this script will only work with a single device from Puppet. 


To get started:
* Copy `env-sample` to `.env`
* Edit `.env` with your environment


An example of the Puppet API query:

```
curl -X GET https://puppet_server.api/pdb/query/v4/facts \

   --data-urlencode 'query=["and", ["=", "name", "DEVICE_NAME"],["=", "name", "networking"]]'
```
