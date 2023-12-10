import requests
import pytest

HOST = 'https://api.pokemonbattle-stage.me:9101'

def test_status_code():
    responce = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 1904})
    assert responce.status_code == 200, ''
    assert responce.json()['trainer_name'] == 'Eduardo', ''