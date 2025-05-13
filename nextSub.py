import requests
import os

PRIM_URL = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"
LINE_13_CODE = "C01383"
STOP_GUY_MOQUET_CODE = "462952"

def get_next_sub():
    """
    
    """

    url = PRIM_URL
    params = {'MonitoringRef': f'STIF:StopPoint:Q:{STOP_GUY_MOQUET_CODE}:',
               'LineRef': f'STIF:Line::{LINE_13_CODE}:'
               }
    
    headers = {
        'apiKey': os.environ['SUBWAY_API_KEY']
        }

    response = requests.request("GET", url, headers=headers, params=params,)

    print(response.text)

if __name__ == "__main__":
    get_next_sub()
