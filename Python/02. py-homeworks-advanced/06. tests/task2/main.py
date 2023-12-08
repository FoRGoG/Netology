import requests

token = ''


def check_status():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': '/'}
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'OAuth {token}'}

    response = requests.get(url, params=params, headers=headers)
    return response
def folder(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'OAuth {token}'}
    if 200 <= check_status().status_code < 300:
        response1 = requests.put(f'{url}?path={path}', headers=headers)
        print(response1.status_code)
        return response1.status_code

name = 'Welcome'
folder(name)
