import requests

# Farmware
from farmware_tools import get_config_value

# Declare vars
headers = {'Content-Type': 'application/json'}
deviceID = get_config_value(farmware_name='SendCmd', config_name='deviceID', value_type=str)
deviceID = get_config_value(farmware_name='SendCmd', config_name='cmd', value_type=str)
payload = {"DeviceName":deviceID, "CmdName":cmd}

resp = requests.post('https://hydrobotapi.azurewebsites.net/api/Hydrobot', json=payload, headers=headers)
print(resp.text)
