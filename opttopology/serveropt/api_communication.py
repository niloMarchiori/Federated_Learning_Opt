#Se comunica com a API do host
import requests

def test_api(api_ip='172.17.0.1', api_port=8000):
    url = f'http://{api_ip}:{api_port}/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
        else:
            print(
                f'Failed to set freq. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')


def set_frequency(api_ip='172.17.0.1', api_port=8000, freq=2.2,trainer_id='sta0'):
    url = f'http://{api_ip}:{api_port}/set_cpufreq/'
    payload = {
        "value": freq,
        "trainer_id": trainer_id
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(response.json())
        else:
            print(
                f'Failed to set freq. Status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error occurred: {e}')