import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': 'c1042ad5f05f25e5041660d00d5e63bb'
}

def test_get_trainers():
    """
    KTI-1 Get trainers status 200
    """
    response = requests.get(url=f'{URL}/trainers', timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_trainers_id():
    """
    KTI-2 Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3611}, timeout=5)
    assert response.json()['trainer_name'] == 'Bloody Nine', ''