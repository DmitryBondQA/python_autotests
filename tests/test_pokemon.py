import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'bd3ecd721b71b1294ebdbfecd6b731e3'

def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {'trainer_id' : 1447})
    assert respons.status_code == 200

def test_name_on_answer():
    respons = requests.get(f'{host}/trainers', params = {'trainer_id' : 1447})
    assert respons.json()['trainer_name'] == 'qte'