import requests
import os

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': 'ZHU-Faded.jpg'}
        headers = {'Authorization': 'OAuth ' + token}
        response = requests.get(url, headers=headers, params=params)
        href = response.json()['href']
        print(href)
        files = {"file": open(os.path.abspath(file_path), "rb")}
        result = requests.post(href, files=files)
        return result


if __name__ == '__main__':
    path_to_file = r'Send_to_yandex_disk/ZHU-Faded.jpg'
    token = 'y0_AgAAAAAE_PNZAADLWwAAAADkr2lHEnBu0_9CSfuOP-KJAsGX4ulwvNI'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

