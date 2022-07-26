from __future__ import annotations

from json import JSONDecodeError
from typing import BinaryIO
from urllib.parse import urlencode

import requests


class ZeroCDN:
    def __init__(self, auth: tuple[str, str], api_key: str, zone: str = None):
        self.auth = auth
        self.api_key = api_key
        self.zone = f'{zone}.' if zone else ''

    def _request(self,
                 path: str,
                 data=None,
                 files=None,
                 method: str = 'POST') -> dict[str, int | str] | str:

        if files is None:
            files = {}
        if data is None:
            data = {}

        url = f'https://{self.zone}mng.zerocdn.com/api/v2/users/{path}'
        if method == 'POST':
            auth = self.auth
        else:
            auth = ()
            url += f"?{urlencode({'username': self.auth[0], 'api_key': self.api_key})}"

        response = requests.request(
            method, url, data=data, auth=auth, files=files
        )
        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    # Работа с файлами

    @staticmethod
    def _params(**params):
        params.setdefault('areas', ['msk.ru', 'minsk2.by'])
        return params

    def upload(self, file: BinaryIO, **params: dict[str]):
        params = self._params(**params)
        return self._request('files.json', params, files=file)

    def upload_from_url(self, url, **params):
        params = self._params(**params)

        return self._request('files.json', {'url': url} | params)

    def files(self, in_folder: int | str = ''):
        return self._request('files.json', {'folder': in_folder}, method='GET')

    def file(self, file_id: int | str):
        return self._request(f'files/{file_id}.json', method='GET')

    def delete_file(self, file_id: int | str):
        return self._request(f'files/{file_id}.json', method='DELETE')

    def rename_file(self, file_id: int | str, new_name: str):
        return self._request(f'files/{file_id}.json', {
            'name': new_name
        }, method='PATCH')

    def change_file(self, file_id: int | str, **params: dict[str]):
        return self._request(f'files/{file_id}.json', params, method='PATCH')

    # Работа с папками

    def create_folder(self, folder_name: str, in_folder: int | str = ''):
        return self._request('folders.json', {'name': folder_name,
                                              'folder': in_folder})

    def folders(self, in_folder: int | str = ''):
        return self._request('folders.json', {'folder': in_folder}, method='GET')

    def folder(self, folder_id: int | str):
        return self._request(f'folders/{folder_id}.json', method='GET')

    def delete_folder(self, folder_id: int | str):
        return self._request(f'folders/{folder_id}.json', method='DELETE')

    def rename_folder(self, folder_id: int | str, new_name: str):
        return self._request(f'folders/{folder_id}.json', {
            'name': new_name
        }, method='PATCH')
