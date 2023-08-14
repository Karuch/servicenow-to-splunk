from jsonpath_ng import jsonpath, parse
import json
from time import sleep
import requests

def get_api_result(url):
    requests.packages.urllib3.disable_warnings() #disables certificate warnings to not interupt the logs.

    user = $user
    pwd = $password

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False) #verify true causes double request for somereason spam API

    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response', response.json())
        exit()

    return response.text

max_units_of_data = 100 #Limit the amount of incidents / outages / changes so it won't spam API

def change():
    quary_request = get_api_result(f"ApiQuaryLink{max_units_of_data}")

    quary = json.loads(quary_request)
    changes_list_encoded = parse('$.result[*]')
    changes_list_decoded = changes_list_encoded.find(quary)

    num = 0

    if len(changes_list_decoded) < 1:
        pass
    else:
        for i in range(1, len(changes_list_decoded) + 1):
            num = 1
    print(f'changes: {num}')

def outage():
    quary_request = get_api_result(f"ApiQuaryLink{max_units_of_data}")

    quary = json.loads(quary_request)
    changes_list_encoded = parse('$.result[*]')
    changes_list_decoded = changes_list_encoded.find(quary)

    num = 0

    if len(changes_list_decoded) < 1:
        pass
    else:
        for i in range(1, len(changes_list_decoded) + 1):
            num = 1
    print(f'outages: {num}')

def ticket():
    quary_request = get_api_result(f"ApiQuaryLink{max_units_of_data}")

    quary = json.loads(quary_request)
    changes_list_encoded = parse('$.result[*]')
    changes_list_decoded = changes_list_encoded.find(quary)

    num = 0

    if len(changes_list_decoded) < 1:
        pass
    else:
        for i in range(1, len(changes_list_decoded) + 1):
            num = 1
    print(f'tickets: {num}')

    if __name__ == '__main__':
        while True:
            ticket()
            change()
            outage()
            sleep(20) #quary the API every 20 seconds intervals