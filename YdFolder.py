from dotenv import load_dotenv
import os.path
import requests


dotenv_path = 'config_example.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
ya_token = os.getenv('YD_TOKEN')


def folder_creation(path: str):
    url = f'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {ya_token}'}
    params = {'path': path}
    response = requests.put(url=url, headers=headers, params=params)

    return response.status_code


def delete_folder(path: str):
    url = f'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {ya_token}'}
    params = {'path': path,
              'permanently': 'true'}
    response = requests.delete(url=url, headers=headers, params=params)

    return response.status_code



