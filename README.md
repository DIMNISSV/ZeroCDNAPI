# ZeroCDNAPI
API for [ZeroCDN](https://zerocdn.com/api)

# Installation
You can
`git clone https://github.com/DIMNISSV/ZeroCDNAPI/`

# Using

```python
from zerocdn import ZeroCDN
zcdn = ZeroCDN((name, pswd))
```

```python
class ZeroCDN:
    def __init__(self, auth: tuple[str, str], api_key: str, zone: str = None):
        ...

    # Working with files / Работа с файлами

    def upload(self, file: BinaryIO, **params: dict[str]):
        ...

    def upload_from_url(self, url, **params):
        ...

    def files(self, in_folder: int | str = ''):
        ...

    def file(self, file_id: int | str):
        ...

    def delete_file(self, file_id: int | str):
        ...

    def rename_file(self, file_id: int | str, new_name: str):
        ...

    def change_file(self, file_id: int | str, **params: dict[str]):
        ...

    # Working with directories / Работа с папками

    def create_folder(self, folder_name: str, in_folder: int | str = ''):
        ...

    def folders(self, in_folder: int | str = ''):
        ...

    def folder(self, folder_id: int | str):
        ...

    def delete_folder(self, folder_id: int | str):
        ...

    def rename_folder(self, folder_id: int | str, new_name: str):
        ...


```
