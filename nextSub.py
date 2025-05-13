import requests


PRIM_URL = "https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring"
LINE_13_CODE = "C01383"
STOP_GUY_MOQUET_CODE = "462952"

def get_next_sub():
    """
    
    """

    url = PRIM_URL
    payload = {'MonitoringRef': STOP_GUY_MOQUET_CODE,
               'LineRef': LINE_13_CODE
               }
    
    headers = {
        'apiKey': SUBWAY_API_KEY
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == "__main__":
    get_next_sub()
    