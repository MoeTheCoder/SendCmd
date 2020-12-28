import requests

# Farmware
from farmware_tools import get_config_value
from farmware_tools import device

# Declare vars
headers = {'Content-Type': 'application/json'}
device.log('Got the header')
deviceID = get_config_value(farmware_name='SendCmd', config_name='deviceID', value_type=str)
device.log('Got the device ID')
cmd = get_config_value(farmware_name='SendCmd', config_name='cmd', value_type=str)
device.log('Got the cmd')
#param1 = get_config_value(farmware_name='SendCmd', config_name='param1', value_type=int)
#param2 = get_config_value(farmware_name='SendCmd', config_name='param2', value_type=int)
payload = {"DeviceName":deviceID, "CmdName":cmd}
device.log('Creatred the payload')

resp = requests.post('https://hydrobotapi.azurewebsites.net/api/Hydrobot', json=payload, headers=headers)
print(resp.text) 
device.log('Finising SendCmd')
