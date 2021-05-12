import requests

# Farmware
from farmware_tools import get_config_value

# Declare vars
headers = {'Content-Type': 'application/json'}
botName = get_config_value(farmware_name='SendCmd', config_name='botName', value_type=str)
device = get_config_value(farmware_name='SendCmd', config_name='device', value_type=str)
cmd = get_config_value(farmware_name='SendCmd', config_name='cmd', value_type=str)
param1 = get_config_value(farmware_name='SendCmd', config_name='param1', value_type=str)
param2 = get_config_value(farmware_name='SendCmd', config_name='param2', value_type=str)
payload = {"BotName":botName, "Device":device, "CmdName":cmd,"Parameter1":param1,"Parameter2":param2}

resp = requests.post('https://hydrobotapi.azurewebsites.net/api/Hydrobot', json=payload, headers=headers)
print(resp.text) 
