import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a1ebd56f5be70dd67fea39bbed7b255'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '4884'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json () ["data"] [0] ["trainer_name"] == 'Котофей'   