import YdFolder
import pytest
import requests
from YdFolder import folder_creation, delete_folder


def test_api_yandex_1():
    assert folder_creation('test_py_1') == 201

def test_api_yandex_2():
    assert folder_creation('test_py_1') == 409

def test_api_yandex_del():
    assert delete_folder('test_py_1') == 204

class TestYDCreateFolder:
    def setup_method(self) -> None:
        self.headers = {
            'Authorization': f'OAuth {YdFolder.ya_token}'
        }

    @pytest.mark.parametrize(
        'param, folder_mame, status',
        (
            ('path', 'test_folder_1', 201),
            ('path', 'test_folder_1', 409),
            ('patthh', 'test_folder_2', 400)
        )
    )
    def test_create_folder(self, param, folder_mame, status):
        params = {
            param: folder_mame
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == status